from rest_framework import serializers

from accounts.serializers import UserSerializer
from todo.models import Task


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    discription = serializers.CharField(max_length=200)
    completed = serializers.BooleanField()

    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)


class TaskSerializerModel(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # source is used to map the field name
    description = serializers.CharField(source="discription")
    # v1 create a new field
    # user_full_name = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()

    def get_info(self, obj):
        return obj.title + " - " + obj.discription

    # def get_user_full_name(self, obj):
    #     return obj.user.get_full_name if obj.user else "No User"

    def to_representation(self, instance):
        # v2 add a new field
        data = super().to_representation(instance)
        data["completed_in_word"] = "Yes" if data["completed"] else "No"
        data["info_v2"] = data["title"]
        return data

    # no need to define fields
    class Meta:
        model = Task
        fields = ["id", "title", "description", "info", "completed"]
        # fields = '__all__'
        # exclude = ['id']
        read_only_fields = ["id"]

        # # error message for fields
        # extra_kwargs = {
        #     # "title": {"error_messages": {"required": "Title is required"}},
        #     "discription": {
        #         "error_messages": {"required": "Discription is majburiy"},
        #         "required": False,
        #     },
        #     "completed": {"error_messages": {"required": "Completed is required"}},
        # }

    # overide save method
    # def save(self, **kwargs):
    #     print("Save", self.validated_data)
    #     return Task.objects.create(**self.validated_data)

    # validate title field
    # def validate_title(self, value):
    #     if "task" not in value:
    #         raise serializers.ValidationError("Title must contain task")
    #     return value

    def validate(self, data):
        self._errors = {}
        if "task" not in data["title"]:
            self._errors["title"] = ["Title must contain task"]
        if self._errors:
            raise serializers.ValidationError(self._errors)
        return data

    def create(self, validated_data):
        print("Create", validated_data)
        user = self.context.get("user")
        validated_data["user"] = user
        return Task.objects.create(**validated_data)

    # overide update method
    def update(self, instance, validated_data):
        print("Update", validated_data)
        instance.title = validated_data.get("title", instance.title)
        instance.discription = validated_data.get("discription", instance.discription)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()
        return instance
