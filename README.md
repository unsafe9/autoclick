# autoclick
Send mouse click event automatically.

## dependencies
- PyQt5
- PyWin32
- PyInstaller

## build
```shell
python --version # >= 3.8
pip install -r ./requirements.txt
pyinstaller --onefile --noconsole ./autoclick.py
```

## 개요
업무시간에 백그라운드로 발헤임 레벨 노가다를 하기 위해 만들었음.

## 사용법
DOWN 에 몇 ms 동안 좌클릭을 누르고 있을건지, UP 에 몇 ms 동안 좌클릭 떼고나서 대기하고 있을건지 지정합니다.<br>
발헤임에 포커스를 두고 있을 때 멈추게 할거면 Background only 선택합니다. 몽둥이 수리하거나 화살 만들 때 매번 끄기 귀찮아서 넣었습니다.
<br><br>
autoclick은 발헤임을 실행한 후 실행합니다. autoclick이 켜져있는 동안 발헤임을 재시작 할 경우 autoclick 또한 재시작해야합니다.

### 발헤임
25 스태미너에 편안함 받을 때 기준 제가 사용하는 값입니다. 레벨 따라 스태미너 소모량이 다르거나 하니 각자 최적으로 조정하면서 사용하세요.
- 달리기
  - 기존 공격 키 변경
  - 달리기 키 좌클릭으로 변경
  - 벽보고 Q(자동달리기) 사용
  - UP 2300, DOWN 9000
- 몽둥이
  - 내구도 다 떨어질 때마다 수리해줘야 한다.
  - UP 200, DOWN 200
- 활
  - 내구도 다 떨어질 때마다 수리해줘야 한다.
  - 화살 다 떨어질 때마다 만들어야 한다.
  - UP 200, DOWN 200