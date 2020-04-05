from django.http import HttpResponse
from django.http import Http404
from polls.models import Question, Choice

from rest_framework import generics
from polls.serializers import QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404


def index(request):
    question_list = Question.objects.all()
    return HttpResponse(', '.join([q.question_text for q in question_list]))


def index_other(request):
    return HttpResponse("Hello, OTHER world. You're at the polls index.")


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj







#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return HttpResponse("You're looking at question %s." % question)


#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    #print(dir(question))
 #   choices = question.choices.all()
#    output = ', '.join([str(c) for c in choices])
#    return HttpResponse(output)


#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
#

#def vote_user(request, question_id, user_id):
#    return HttpResponse("You're voting on question {}. for user {}".format(question_id, user_id))


