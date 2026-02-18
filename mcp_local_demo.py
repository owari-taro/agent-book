#!/usr/bin/env python3
"""
MCPローカルファイルシステム デモ

このスクリプトは、ローカルファイルシステムMCPサーバーの使用例を示します。
ネットワーク接続は不要で、Node.js環境があれば実行できます。
"""

import asyncio
import os
import sys
from pathlib import Path


async def test_local_mcp():
    """ローカルファイルシステムMCPサーバーをテストします"""
    print("=" * 70)
    print("MCP ローカルファイルシステム デモ")
    print("=" * 70)
    print()
    
    # Node.jsとnpxの存在確認
    print("🔍 環境チェック中...")
    try:
        import subprocess
        result = subprocess.run(['npx', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print(f"✅ npx が見つかりました (version: {result.stdout.strip()})")
        else:
            print("❌ npx が見つかりませんでした")
            print("   Node.js と npm のインストールが必要です")
            return False
    except Exception as e:
        print(f"❌ npx チェックでエラー: {str(e)}")
        print("   Node.js と npm のインストールが必要です")
        return False
    
    print()
    print("📝 MCPの設定:")
    print("-" * 70)
    
    config = {
        "server_name": "file-system",
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem@2025.7.1",
            str(Path.cwd())
        ],
        "transport": "stdio"
    }
    
    print(f"Server: {config['server_name']}")
    print(f"Command: {config['command']}")
    print(f"Package: {config['args'][1]}")
    print(f"Working Directory: {config['args'][2]}")
    print(f"Transport: {config['transport']}")
    print()
    
    print("✨ このMCPサーバーの機能:")
    print("-" * 70)
    features = [
        "ファイルの読み取り",
        "ファイルの書き込み",
        "ディレクトリの一覧表示",
        "ファイルの検索",
        "ファイル情報の取得"
    ]
    for feature in features:
        print(f"  ✓ {feature}")
    
    print()
    print("=" * 70)
    print("📚 使用例:")
    print("=" * 70)
    print()
    
    example_code = """
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph

# MCPクライアントの初期化
mcp_client = MultiServerMCPClient({
    "file-system": {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem@2025.7.1",
            "./"
        ],
        "transport": "stdio",
    }
})

# ツールを取得
tools = await mcp_client.get_tools()

# LLMにツールをバインド
llm = init_chat_model(
    model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    model_provider="bedrock_converse",
)
llm_with_tools = llm.bind_tools(tools)

# エージェントで使用
# これで、AIエージェントがローカルファイルシステムにアクセスできます！
"""
    print(example_code)
    
    print()
    print("=" * 70)
    print("✅ MCPローカルファイルシステムサーバーは使用可能です！")
    print("=" * 70)
    print()
    print("💡 ヒント:")
    print("  完全な動作例は chapter4/3_mcp_agent.py を参照してください。")
    print("  このファイルには、AWS Bedrock と統合された実際の動作例が含まれています。")
    
    return True


def main():
    """メイン関数"""
    try:
        success = asyncio.run(test_local_mcp())
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n中断されました。")
        return 1
    except Exception as e:
        print(f"\nエラーが発生しました: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
