import urllib.request
import json

def test_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    try :
        print("Menguji koneksi API...")
        response = urllib.request.urlopen(url, timeout=5)
        data_json = response.read().decode('utf-8')
        data = json.loads(data_json)
        print("Berhasil mengambil data dari API!")
        print("menampilkan 3 judul pertama:\n")
        for i, post in enumerate(data[:3], start=1):
            print(f"{i}.{post['title']}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error:{e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error:{e.reason}")
    except Exception as e:
        print(f"Error tak terduga: {e}")
        
if __name__== "__main__":
    test_api()