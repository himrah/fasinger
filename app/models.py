from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    birth_day = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.user)

"""    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()         """   




class Profile_pic(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    profile_original = models.ImageField(upload_to='photos/profile/original')
    profile_thumbs = models.ImageField(upload_to='photos/profile/thumbs')
    profile_photo = models.ImageField(upload_to='photos/profile/photo')

    def __str__(self):
        return (self.profile.user.username)

    def save(self):
        im = Image.open(self.profile_original)
        output = BytesIO()
        basewidth = 600
        #img = Image.open('somepic.jpg')
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)      
        im = im.convert("RGB")
        im.save(output, format='JPEG', quality=70)
        
        self.profile_photo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.profile_original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        
        weight,height=im.size
        if weight > height:
            r=(weight-height)/2
            imc=im.crop((r,0,height+r,height))
        else:
            r=(height-weight)/2
            imc=im.crop((0,r,weight,height-r))  
        imc = imc.convert("RGB")      
        imc=imc.resize((300,300),Image.ANTIALIAS)
        output = BytesIO()
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.profile_thumbs = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.profile_original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Profile_pic,self).save()


class Photos(models.Model):
    #pic_name=models.CharField(max_length=20)
    original_photo=models.ImageField(upload_to='photos/original')
    thumbs = models.ImageField(upload_to='photos/thumbs/')
    photo = models.ImageField(upload_to='photos/photo')
    created_date=models.DateTimeField(default=datetime.now,null=True)
    #comment=models.TextField()
    upload_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.upload_by)+' : '+str(self.created_date)

    def save(self):
        super(Photos,self).save()
        im = Image.open(self.original_photo)
        output = BytesIO()
        basewidth = 600
        #img = Image.open('somepic.jpg')
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)      
        im = im.convert("RGB")
        im.save(output, format='JPEG', quality=70)
        
        self.photo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original_photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)




        
        weight,height=im.size
        if weight > height:
            r=(weight-height)/2
            imc=im.crop((r,0,height+r,height))
        else:
            r=(height-weight)/2
            imc=im.crop((0,r,weight,height-r))  
        imc = imc.convert("RGB")      
        imc=imc.resize((300,300),Image.ANTIALIAS)
        output = BytesIO()
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.thumbs = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original_photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)






        """weight,height=im.size
        output = BytesIO()
        left = (weight - 300)/2
        top = (height - 300)/2
        right = (weight + 300)/2
        bottom = (height + 300)/2

        imc = im.crop((left, top, right, bottom))"""
        
        #new_height = 680
        #new_width  = new_height * width / height
        #new_width=680
        #im = im.resize((new_width, new_height), Image.ANTIALIAS)
        #im = im.resize( (100,100))
        #self.thumbs = output
        #output = BytesIO()
        #imcc=imc.resize((300,300),Image.ANTIALIAS)
        #imcc.save(output, format='JPEG', quality=40,optimize=True)

        #output.seek(0)
        #self.thumbs = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original_photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        #super(Photos,self).save()


class Comments(models.Model):
    photo_id = models.ForeignKey(Photos, related_name='comments', on_delete=models.CASCADE,null=True)
    comment_time = models.DateTimeField(default=datetime.now,null=True)
    #upload_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='%(class)s_upload_by')
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #comment = models.CharField(max_length=100, null=True)
    comment = models.TextField()
    def __str__(self):
        return str(self.photo_id)+' : '+str(self.comment_by)
    


        


        """        weight,height=im.size
        if weight > height:
            r=(weight-height)/2
            imc=im.crop((r,0,height+r,height))
        else:
            r=(height-weight)/2
            imc=im.crop((0,r,weight,height-r))  
        imc = imc.convert("RGB")      
        imc=imc.resize((600,600),Image.ANTIALIAS)
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.photo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original_photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
"""