from rest_framework import serializers
from .models import FormType, FormSubmission

class FormTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormType
        fields = ['id', 'name', 'description']

class FormSubmissionSerializer(serializers.ModelSerializer):
    region = serializers.ChoiceField(
        choices=FormSubmission.REGION_CHOICES, 
        required=False, allow_blank=True
    )
    form_type = FormTypeSerializer(read_only=True)
    form_type_id = serializers.PrimaryKeyRelatedField(
        queryset=FormType.objects.all(), source='form_type', write_only=True
    )

    class Meta:
        model = FormSubmission
        fields = [
            'id', 'form_type', 'form_type_id', 'full_name', 'email', 'phone',
            'region', 'content', 'data', 'is_approved',
            'submitted_at', 'reviewed_at', 'reviewer'
        ]
        read_only_fields = [
            'id', 'is_approved', 'submitted_at', 'reviewed_at', 'reviewer', 'form_type'
        ]

    def validate(self, data):
        # Require region only for registration
        form_type = data.get('form_type')
        region = data.get('region')
        if form_type and form_type.name.lower() == "registration":
            if not region:
                raise serializers.ValidationError({"region": "This field is required for registration."})
        return data
