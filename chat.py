#!/usr/bin/env python3
"""
IBM Quantum / Qiskit リソース案内チャットボット
A simple conversational chatbot to guide users through IBM Quantum / Qiskit resources.
"""

import re

# Knowledge base: keyword patterns mapped to responses
FAQ = [
    (
        r"ibm\s*quantum\s*composer|composer",
        "IBM Quantum Composer は、ブラウザー上で量子回路の設計・実行・結果表示ができる GUI ツールです（無料）。\n"
        "▶ https://quantum-computing.ibm.com/composer",
    ),
    (
        r"ibm\s*quantum\s*lab|lab",
        "IBM Quantum Lab は、Qiskit をインストールなしで実行できる Jupyter Notebook 環境です（無料）。\n"
        "▶ https://lab.quantum-computing.ibm.com",
    ),
    (
        r"テキストブック|textbook|教科書",
        "Qiskit テキストブック日本語版では量子情報の基礎から量子アプリケーションまで学べます。\n"
        "▶ https://qiskit.org/textbook/ja/preface.html",
    ),
    (
        r"チュートリアル|tutorial",
        "Qiskit ドキュメント チュートリアル（日本語）で Qiskit の使い方を学べます。\n"
        "▶ https://qiskit.org/documentation/locale/ja_JP/index.html",
    ),
    (
        r"チャレンジ|challenge|コンテスト",
        "IBM Quantum Challenge は量子プログラミングコンテストで、初心者から学習できる教材もあります。\n"
        "過去の問題: https://github.com/quantum-challenge/2019",
    ),
    (
        r"advocate|アドボケート",
        "Qiskit Advocate は毎年夏ごろに募集があります。\n"
        "▶ https://github.com/qiskit-advocate/application-guide",
    ),
    (
        r"認定|certification|資格",
        "Qiskit デベロッパー認定制度があります。\n"
        "▶ https://www.ibm.com/training/certification/C0010300",
    ),
    (
        r"翻訳|translation",
        "Qiskit 翻訳活動に参加できます。\n"
        "▶ https://github.com/qiskit-community/qiskit-translations",
    ),
    (
        r"quantum\s*tokyo|勉強会|イベント",
        "Quantum Tokyo は日本国内の Qiskit 勉強会で、月に１〜２回オンライン開催しています。\n"
        "イベント告知: https://quantum-tokyo.connpass.com/\n"
        "録画: https://www.youtube.com/channel/UCT_lkXOYYBIbfk8CnvQ6Heg",
    ),
    (
        r"機械学習|machine\s*learning",
        "量子機械学習のチュートリアルがあります。\n"
        "▶ https://qiskit-community.github.io/qiskit-translations-staging/apps/machine-learning/ja_JP/",
    ),
    (
        r"研究者|researcher|researcher program",
        "IBM Quantum 研究者プログラム（無料）では、優先アクセス権などが得られます。\n"
        "▶ https://quantum-computing.ibm.com/programs/researchers",
    ),
    (
        r"教育|educator|教員|先生",
        "IBM Quantum 教育用プログラム（無料）では、授業やワークショップで量子デバイスを優先利用できます。\n"
        "▶ https://quantum-computing.ibm.com/programs/educators",
    ),
    (
        r"はじめ|始め|入門|start|begin|初心者",
        "初心者には IBM Quantum Composer がおすすめです。\n"
        "▶ https://quantum-computing.ibm.com/composer\n"
        "Qiskit テキストブック日本語版も参考にどうぞ。\n"
        "▶ https://qiskit.org/textbook/ja/preface.html",
    ),
    (
        r"qiskit\s*install|インストール",
        "Qiskit は pip でインストールできます: `pip install qiskit`\n"
        "インストール不要で試すには IBM Quantum Lab をご利用ください。\n"
        "▶ https://lab.quantum-computing.ibm.com",
    ),
    (
        r"リンク|link|一覧|list",
        "IBM Quantum / Qiskit 関連リンク集は README.md にまとめてあります。\n"
        "▶ https://github.com/ibmbob/introduction/blob/main/README.md",
    ),
]

GREETING_PATTERNS = re.compile(
    r"^(こんにちは|hello|hi|hey|はじめまして|よろしく)", re.IGNORECASE
)
EXIT_PATTERNS = re.compile(
    r"^(exit|quit|bye|さようなら|終了|おわり|ありがとう|thanks)", re.IGNORECASE
)


def find_response(user_input: str) -> str:
    text = user_input.lower()
    for pattern, response in FAQ:
        if re.search(pattern, text, re.IGNORECASE):
            return response
    return (
        "申し訳ありませんが、その質問には答えられません。\n"
        "以下のキーワードで質問してみてください：\n"
        "  composer, lab, textbook, tutorial, challenge, advocate,\n"
        "  certification, translation, quantum tokyo, machine learning,\n"
        "  researcher, educator, install, リンク"
    )


def chat() -> None:
    print("=" * 60)
    print("IBM Quantum / Qiskit リソース案内チャットボット")
    print("IBM Quantum / Qiskit Resource Guide Chatbot")
    print("=" * 60)
    print("質問を入力してください（終了するには 'exit' と入力）。")
    print("Type your question (type 'exit' to quit).")
    print()

    while True:
        try:
            user_input = input("あなた / You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nさようなら！ / Goodbye!")
            break

        if not user_input:
            continue

        if EXIT_PATTERNS.match(user_input):
            print("ボット: ありがとうございました！またご利用ください。 / Bot: Thank you! Goodbye!")
            break

        if GREETING_PATTERNS.match(user_input):
            print("ボット: こんにちは！IBM Quantum / Qiskit について何でも聞いてください。")
            print()
            continue

        response = find_response(user_input)
        print(f"ボット: {response}")
        print()


if __name__ == "__main__":
    chat()
