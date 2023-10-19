import pandas as pd
from GoogleNews import GoogleNews


googlenews = GoogleNews()
googlenews.set_lang('pt-br')
googlenews.set_period('3d')
googlenews.set_encode('utf-8')
googlenews.search("Israel")
top = googlenews.get_news("Israel")
result = googlenews.result(sort=True)
print(result[0])
print(top[0])
#for result in result:
#    print(result['title'])

#print(googlenews.page_at(2))



#data = pd.DataFrame.from_dict(result)
#data.head()
#print(data)