# UNIT-PROJECT-3


## Create a Personal Website


A personal website is website that represents you , your work , your career , your interests and so on. It could be highly stylish , fun, or simple, serious and so on. You choose how you represent yourself online !



### Inspirations:
- https://www.shanekinkennon.com
- https://www.joshrubietta.com
- https://www.jencarrington.com
- https://www.amywutoo.com
- https://www.ginakirlew.com


## Minimum Requirements
- At minimum 4 pages.
- Use a CSS library to style your website.
- User Login & Sign up.
- Services App.
- Use is_authenticate, is_staff , etc. to limit access to some pages / functionality.

### Services App
Users should be able to view services you provide , then request a service. to acheive this , you need the following:

#### Service Model
  - title
  - description
  - image
  - created_at
You can add more fields as needed.

#### ServiceRequest Model
- relation with user
- relation with service
- status (pending, in_progress, done, canceled)
You can add more fields as needed.


#### Pages in services :
- Add / update  pages for the Service model.
- A page to disply your services for the users.
- A detail page to show the service.
- Users can request a service in the detail page.
- A manager page to manage the service requests you receive.
- A My Requests page so the user can display the services he/she requested and the status of it.

for staff :
 1- add page
 2- update page
for users:
3-detail page
4- reques page for user
for admain:
5-manager page 







## Resources:

### Free high quality images :
- https://www.pexels.com/
- https://unsplash.com


### Free sounds website:
- https://mixkit.co/

### Free stock videos:
- https://pixabay.com/videos/

### Free Fonts:
- https://fonts.google.com

### Free Icons
- https://fonts.google.com/icons
- https://icons.getbootstrap.com/


### CSS Library:
- https://getbootstrap.com/
- https://get.foundation/index.html

### CSS Animation libraries:
- https://animate.style
- https://www.minimamente.com/project/magic/







{% extends 'main/base.html' %}


{% block title %} {{request.user.first_name}} requests  {% endblock %}

{% block content %}

<h2>{{request.user.first_name}} requests </h2>

{% for requests in reqs %}

    <div class="d-flex gap-2 p-4 m-2">
        <img src="{{requests.logo.image.url }}" class="small-poster object-fit-cover rounded-4" />
        <div>
            <h3><a href="{% url 'services:logo_detail_view' requests.logo.id %}">{{ requests.logo.title }}</a></h3>
            <h5>{{ requests.logo.description }}</h5>
        </div>
    </div>

{% endfor %}

{% endblock %}



from django.contrib.auth.models import User

def user_requests_view(request: HttpRequest):
    user=request.user
    user_request=Requests.objects.filter(user=user)


    return render(request, 'services/requests_page.html',{"reqs":user_request})

