from django.shortcuts import render, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
import json

with open('./foodservise/q1.json') as json_data:
	d = json.load(json_data)
	json_data.close()


class get_food_service(APIView):
	@staticmethod
	def get(request):
		return Response(d["q"])

	def post(self, request):
		# print( self.request.query_params.get("ans"))
		if self.request.query_params.get("ans") == "yes":
			if self.request.query_params.get("state") == "0":
				return Response(d["a"]["yes"]["q"])
			elif self.request.query_params.get("state") == "1":
				print(d["q"], ": Yes -> Pizza -> Yes")
				return Response(d["a"]["yes"]["a"]["Pizza"]["a"]["yes"])
			else:
				print(d["q"], ": error happend ->", self.request.query_params.get("ans"))
				raise Http404("invalid request")

		elif self.request.query_params.get("ans") == "no":
			if self.request.query_params.get("state") == "0":
				print(d["q"], ": No ")
				return Response(d["a"]["no"])
			elif self.request.query_params.get("state") == "1":
				print(d["q"], ": Yes -> Pizza -> No")
				return Response(d["a"]["yes"]["a"]["Pizza"]["a"]["no"])
			else:
				print(d["q"], ": error happend ->", self.request.query_params.get("ans"))
				raise Http404("invalid request")
		elif self.request.query_params.get("ans") == "Hamburger":
			print(d["q"], ": Yes -> Hamburger ")
			return Response(d["a"]["yes"]["a"]["Hamburger"])
		elif self.request.query_params.get("ans") == "Pizza":
			return Response(d["a"]["yes"]["a"]["Pizza"]["q"])
		elif self.request.query_params.get("ans") == "Pop Corn":
			print(d["q"], ": Yes -> Pop Corn ")
			return Response(d["a"]["yes"]["a"]["Pop Corn"])
		elif self.request.query_params.get("ans") == "Chicken":
			print(d["q"], ": Yes -> Chicken ")
			return Response(d["a"]["yes"]["a"]["Chicken"])
		else:
			print(d["q"], ": error happend ->", self.request.query_params.get("ans"))
			raise Http404("invalid request")


def homepage(request):
	return render(request, 'index.html')
# Create your views here.
