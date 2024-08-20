#!/bin/python3

def showInstructions():
  # 印刷メインメニューとコマンド
  print('''
RPGゲーム
========
コマンド：
  行く [方向]
  取得する [項目]
''')

def showStatus():
  # 選手の現在のステータスを表示する
  print('---------------------------')
  print('あなたは' + currentRoom + 'にいる')
  # 現在の インベントリー
  print('インベントリー : ' + str(inventory))
  # 項目があればそれを表示する
  if '項目' in rooms[currentRoom]:
    print(rooms[currentRoom]['項目'] + 'が見える')
  print('---------------------------')

# インベントリ（最初は空)
inventory = []

# 部屋と他の部屋を結ぶ辞書
rooms = {

    'ホール' : {
        '南に' : 'キッチン'
    },

    'キッチン' : {
        '北に' : 'ホール'
    }


}

# ホールでスタート選手
currentRoom = 'ホール'

showInstructions()

# 永遠ループ
while True:

  showStatus()

  # 選手の次の「一手」を得る
  # .split() でリスト配列に分割す
  # 例：タイピング '東に 行く' がリストを出すだろう：
  # ['東に','行く']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  # 最後に'行く'と打つと
  if move[1] == '行く':
    # 行きたいところに行けるか確認する
    if move[0] in rooms[currentRoom]:
      # 現在の部屋を新しい部屋に設定する
      currentRoom = rooms[currentRoom][move[0]]
    # 新しい部屋へのドア（リンク）がない
    else:
        print('あそこには行けないよ！')

  # 最後に'取得する'と打つと
  if move[1] == '取得する' :
    # 部屋にアイテムがあり、そのアイテムが手に入れたいものである場合
    if '項目' in rooms[currentRoom] and move[0] in rooms[currentRoom]['項目']:
      # アイテムをインベントリに追加する
      inventory += [move[0]]
      # 役立つメッセージを表示する
      print(move[0] + 'は手に入れた！')
      # 部屋からアイテムを削除する
      del rooms[currentRoom]['項目']
    # そうでなければ、もしそのアイテムがそこになければ
    else:
      # 手に入らないと言う
      print(move[0] + 'が見つかりません！')
