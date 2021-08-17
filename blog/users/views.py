from django.shortcuts import render
from django.views import View

class RegisterView(View):
    '''
    用户注册
    '''
    def get(self, request):
        '''

        :param request:
        :return:
        '''
        return render(request, 'register.html')