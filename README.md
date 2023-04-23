# chatgpt_read_aloude
Anaconda
python3.11
flask
chatgptと音声で会話するためのプログラム macにて動作確認
chatgpt,whisperを利用しているため、トークンの消費量が多い
使用する場合は　export OPENAI_API_KEY="自分のAPIKEY"

# 使い方
enter→録音停止
exitと入力→プログラム終了

# todolist
和訳英訳を使用してトークンを節約する
録音が強制で30sなので修正

# メモ anaconda起動後
cd webapp
flask run
