from django.db import models

# About Me Section
class AboutMe(models.Model):
        name = models.CharField(max_length=20)
        profile_img = models.ImageField(upload_to='profile/')
        heading = models.CharField(max_length=50)
        career = models.CharField(max_length=20)
        description = models.TextField(blank=False)

        # Update when modified
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.career


# Social media links
class Profile(models.Model):
        about = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
        social_name = models.CharField(max_length=10)
        social_link = models.URLField(max_length=200)


# Work Skills
class Category(models.Model):
        name = models.CharField(max_length=20)
        updated = models.DateTimeField(auto_now=True)

        class Meta:
                verbose_name = 'Skill'
                verbose_name_plural = 'Skills'
        
        def __str__(self):
                return self.name


class Skills(models.Model):
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        skill_name = models.CharField(max_length=20)


# Contains projects
class Project(models.Model):
        title = models.CharField(max_length=30)
        image = models.ImageField(upload_to='project_img/')
        link = models.URLField(max_length=200)

        def __str__(self):
                return f'Portfolio {self.id}'
 
