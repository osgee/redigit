from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from redigit import clf


capacity = 10
pointer = 0


def index(request):
    t = loader.get_template("index.html")
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))


@csrf_exempt
def predict(request):
    result=6
    try:
        imgdata = request.POST['img']
        imgbase64 = str(imgdata).replace('data:image/png;base64,', "")
        imagename = "digits/image_"+str(clf.pointer % 100)+".png"
        digitsname = "digits/digit_"+str(clf.pointer % 100)+".jpg"
        clf.pointer = clf.pointer+1
        fh = open(imagename, "wb")
        data = imgbase64.decode('base64')
        fh.write(data)
        fh.close()
        data = clf.get_image_data(imagename)
        clf.save_image(data, digitsname)
        preds = clf.dp.predict_image(data)
        result = preds
    except KeyError as e:
        # Redisplay the question voting form.
        # return render(request, 'polls/detail.html', {
        #     'question': p,
        #     'error_message': "You didn't select a choice.",
        # })
        # print "error_message"
        # return HttpResponse("Your predict is %s." % result)
        return HttpResponseRedirect(reverse('index'))
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        return HttpResponse("My predict is %s." % result)
        # pass
        # name = request.POST.get('name')
        # return HttpResponse(json.dumps({'name': name}), content_type="application/json")
