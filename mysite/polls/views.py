from django.http import HttpResponse
import requests
import pdb
import json
from rest_framework.decorators import list_route
from django.views.decorators.csrf import csrf_exempt



@list_route(methods=['POST'])
@csrf_exempt
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    #geodata = {}
    pdb.set_trace()
    url = 'https://www.googleapis.com/youtube/v3/search?part=id&q=' + request.POST.get('searchkey') + '&maxResults=3&type=video&key=AIzaSyC8b5oxz-lLC3XqFBSNOpH49IyfTpt6nmk'
    response = requests.get(url)
    #print(response.json())
    #geodata = response.json()
    #response={
    #    'ip': geodata['ip'],
    #    'country': geodata['country_name']
    #}
    return HttpResponse("Awesome")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
