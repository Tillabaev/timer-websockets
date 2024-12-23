from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TimerControlView(APIView):
    def post(self,request,*args,**kwargs):
        action = request.data.get('action')
        if action == 'stop':
            return Response({'message':'Таймер остановлен'},status=status.HTTP_200_OK)
        return Response({'message':'Неверное действие'},status=status.HTTP_400_BAD_REQUEST)
