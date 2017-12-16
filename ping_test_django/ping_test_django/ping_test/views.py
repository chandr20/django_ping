from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from .forms import ServerIplistForm
from django.views.generic.base import TemplateView
from .models import Serveriplist, PingJobuid
from django.views import View
from django.http import HttpResponse
from .ping_tester import Record_Ping
import uuid
import _thread
from django.http import Http404


def ping_data(ip, pk):
    ping_record = Record_Ping(ip)
    samp = ping_record.perform_test()
    Ipinfo = Serveriplist.objects.get(pk=pk)

    Ipinfo.Sent = samp[0]
    Ipinfo.Recieved = samp[1]
    Ipinfo.Lost = samp[2]

    if Ipinfo.Sent and Ipinfo.Recieved and Ipinfo.Lost is None:
        Ipinfo.Ping_Job.State = "Failed"
    else:
        Ipinfo.Ping_Job.State = "Finished"
    Ipinfo.Ping_Job.save()
    Ipinfo.save()


class Serverlist(CreateView):
    form_class = ServerIplistForm
    template_name = 'form.html'
    success_url = '/Iplist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Server Ips'
        return context

class Dellist(DeleteView):
    form_class = ServerIplistForm
    template_name = 'form.html'
    success_url = '/Iplist'
    model = Serveriplist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DEL Server Ips'
        return context


class IpListView(TemplateView):
    template_name = 'iplist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['server_ips'] = Serveriplist.objects.all()
        return context


class Ipaction(View):
    def get(self, request, *args, **kwargs):
        Ipinfo = Serveriplist.objects.get(pk=kwargs['pk'])
        pk = kwargs['pk']
        if Ipinfo.Ping_Job is None:
            PingGuid = str(uuid.uuid4())
            PingJobuid_instance = PingJobuid()
            PingJobuid_instance.PingGuid = PingGuid
            PingJobuid_instance.save()
            Ipinfo.Ping_Job = PingJobuid_instance
            Ipinfo.save()
            try:
                _thread.start_new_thread(ping_data, (Ipinfo, pk))
            except:
                Ipinfo.Ping_Job.State = "Failed"
                Ipinfo.Ping_Job.save()

            return HttpResponse(Ipinfo.Ping_Job)
        else:
            return HttpResponse("Already job is under process")


class Reset(View):
    def get(self, request, *args, **kwargs):
        Ipinfo = Serveriplist.objects.get(pk=kwargs['pk'])
        Ipinfo.Ping_Job = None
        Ipinfo.Sent = None
        Ipinfo.Recieved = None
        Ipinfo.Lost = None
        Ipinfo.save()
        return HttpResponse("Reset Done")


class JobStatus(View):
    def get(self, request, *args, **kwargs):
        jobstatus = PingJobuid.objects.get(PingGuid=kwargs['job'])
        return HttpResponse(jobstatus.State)



        # Create your views here.
