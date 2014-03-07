from django.conf import settings
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, CharField, ToOneField
from tastypie.resources import ModelResource, Resource
from lecture.models import Student, Class, Project, StudentProject


class BareClassResource(ModelResource):
    class Meta:
        queryset = Class.objects.all()
        resource_name = "bare_class"

class StudentResource(ModelResource):
    klass = ToOneField(BareClassResource, 'klass', full=True)

    class Meta:
        queryset = Student.objects.all()
        resource_name = "student"
        authorization = Authorization()

class StudentProjectResource(ModelResource):
    class Meta:
        queryset = StudentProject.objects.all()
        resource_name = "project"
        authorization = Authorization()


class ClassResource(ModelResource):
    students = ToManyField(StudentResource, 'students', full=True, null=True)

    class Meta:
        queryset = Class.objects.all()
        resource_name = "class"
        authorization = Authorization()
        filtering = {
            'students': ALL_WITH_RELATIONS,
            'title': ['contains', 'icontains'],
            'start_date': ['gt',]
        }


######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)