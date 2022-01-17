@echo off
cd /d %~dp0

REM python tools\rename.py test_pic

for /l %%n in (0,1,0) do (
    if not exist predict_cache\img%%n (
        mkdir predict_cache\img%%n
        echo make dir predict_cache\img%%n
    )
    echo predict img%%n
    python main.py test_pic/img%%n.jpg predict_cache/img%%n > result%%n.txt
)
pause