# 開發說明
## 使用虛擬環境(可以不用)
```
$ python -m venv THRS
$ cd THRS
$ source bin/activate
$ pip install django
```
## coding introduction
* static 可以放網頁的靜態元素 (css,image......)
* 網頁會從`urls.py` 執行後面的function(`views.py`)
* `models.py`：放資料表欄位資訊的地方
* html放在`reservation/templates`