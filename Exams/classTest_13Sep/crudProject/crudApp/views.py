from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import json


#POST
def create_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.create(namme = data['name'], description=data['description'])
        return JsonResponse({'message':'Item created','item':{'name': item.name, 'description': item.description}})
    
#PUT
@csrf_exempt
def update_item(request, item_id):
    if request.method == 'PUT':
        try:
            item = Item.onjects.get(id = item_id)
        except Item.DoesNotExist:
            return JsonResponse({'error':'Item not found'}, status=404)
        
        data =  json.loads(request.body)
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.save()

        return JsonResponse({'message':'Item updated', 'item': {'name':item.name,'description':item.description}})
    
#DELETE
@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        try:
            item = Item.onjects.get(id = item_id)
        except Item.DoesNotExist:
            return JsonResponse({'error':'Item not found'}, status=404)
        
        item.delete()
        return JsonResponse({'message':'Item deleted'})
