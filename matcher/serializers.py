from rest_framework import serializers


class MatchRequestSerializer(serializers.Serializer):
    resume_text = serializers.CharField(required=False, allow_blank=True)
    resume_file = serializers.FileField(required=False)
    jd_text = serializers.CharField(required=True, allow_blank=False)

    def validate(self, data):
        if not data.get("resume_text") and not data.get("resume_file"):
            raise serializers.ValidationError(
                "Provide either resume_text or resume_file."
            )
        return data


class SkillBreakdownSerializer(serializers.Serializer):
    matched = serializers.ListField(child=serializers.CharField())
    missing = serializers.ListField(child=serializers.CharField())


class ExplanationSerializer(serializers.Serializer):
    summary = serializers.CharField()
    suggestions = serializers.ListField(child=serializers.CharField())


class MatchResponseSerializer(serializers.Serializer):
    score = serializers.IntegerField()
    must_have_skills = SkillBreakdownSerializer()
    nice_to_have_skills = SkillBreakdownSerializer()
    explanation = ExplanationSerializer()