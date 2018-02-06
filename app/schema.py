from django.contrib.auth.models import User,Group

from .models import Comments,Photos
from graphene import ObjectType,Node,Schema,List,Field,relay,AbstractType
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
"""
class Owner(DjangoObjectType):
    class Meta:
        model = User
        #fields = ('username','first_name','last_name')
        interfaces = (relay.Node)"""

"""
class UserNode(DjangoObjectType):
    class Meta:
        model = Group
        #fields = ('username','first_name','last_name')
        interfaces = (relay.Node)
"""

class PhotoType(DjangoObjectType):
    class Meta:
        model = Photos

class CommentType(DjangoObjectType):
    class Meta:
        model = Comments



class PhotoNode(DjangoObjectType):
    class Meta:
        model = Photos
        filter_fields = ['id']
        interfaces = (relay.Node,)

class CommentNode(DjangoObjectType):
    #photos = List(PhotoNode)
    class Meta:
        model = Comments
        filter_fields = ['id','comment']
        interfaces = (relay.Node,)
    #def resolve_photos(self):
        #return self.photos.all()    

import graphene
class Query(AbstractType):

#    owner = relay.Node.Field(Owner)
#    all_owner = DjangoFilterConnectionField(Owner)
    
    #users = relay.Node.Field(UserNode)
    #all_users = DjangoFilterConnectionField(UserNode)

#    photo = relay.Node.Field(PhotoType)
 #   comment = relay.Node.Field(CommentType)
    photo = Field(PhotoType,id=graphene.Int(),name=graphene.String())
    all_photos = graphene.List(PhotoType)

    comment = Field(CommentType,id=graphene.Int(),name=graphene.String())
    all_comments = graphene.List(CommentType)

#    photos = relay.Node.Field(PhotoNode)
#    all_photos = DjangoFilterConnectionField(PhotoNode)

#    comments = relay.Node.Field(CommentNode)
#    all_comments = DjangoFilterConnectionField(CommentNode)


    def resolve_all_photos(self,info,**kwargs):
        return Photos.objects.all()
    def resolve_all_comments(self,info,**kwargs):
        return Comments.objects.select_related('photo_id').all()    

#schema = Schema(query=Query)



"""class Query(Abs):
    all_photos = List(PhotoNode)
    all_comments = List(CommentNode)
    
    #debug = Field(DjangoDebug, name='__debug')
    photos = Node.Field(PhotoNode)
    #all_photos = DjangoConnectionField(PhotoNode)

    comments = Node.Field(CommentNode)
    #all_comments = DjangoConnectionField(CommentNode)

    def resolve_all_photos(self,info, **kwargs):
        return Photos.objects.all()

    def resolve_all_comments(self,info,**kwargs):
        #return Comments.objects.all()
        return  Comments.objects.select_related('photo').all()

    #@resolve_only_args
    def resolve_photos(self,info,**kwargs):
        
        id = kwargs.get('id')
        if id is not None:
            return Photos.objects.get(pk=id)
        return None    

    def resolve_comments(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Comments.objects.get(pk=id)
        return None    """