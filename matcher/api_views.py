from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MatchRequestSerializer, MatchResponseSerializer
from .services.extractor import extract_skills, extract_text_from_pdf
from .services.scorer import compute_match, generate_explanation
from .models import MatchResult


class MatchView(APIView):
    def post(self, request):
        serializer = MatchRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if data.get("resume_file"):
            resume_text = extract_text_from_pdf(data["resume_file"])
        else:
            resume_text = data.get("resume_text", "")

        jd_text = data["jd_text"]

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        match_data = compute_match(resume_skills, jd_skills)
        explanation = generate_explanation(match_data)

        response_data = {**match_data, "explanation": explanation}

        MatchResult.objects.create(
            resume_text=resume_text,
            jd_text=jd_text,
            score=match_data["score"],
            must_have_matched=match_data["must_have_skills"]["matched"],
            must_have_missing=match_data["must_have_skills"]["missing"],
            nice_to_have_matched=match_data["nice_to_have_skills"]["matched"],
            nice_to_have_missing=match_data["nice_to_have_skills"]["missing"],
            summary=explanation["summary"],
            suggestions=explanation["suggestions"],
        )

        response_serializer = MatchResponseSerializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_200_OK)