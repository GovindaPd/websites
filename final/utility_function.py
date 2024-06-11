from datetime import datetime
import content

def getcontext():
   context = {}
   context['title'] = content.title
   context['websitename'] = content.websitename
   context['currentyear'] = datetime.today().year
   context['instruction'] = ""
   return context