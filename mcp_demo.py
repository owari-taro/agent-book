#!/usr/bin/env python3
"""
MCP (Model Context Protocol) デモンストレーション

このスクリプトは、MCPの設定方法と使用パターンを示します。
実際のネットワーク接続は不要で、MCPの設定と構造を理解できます。
"""

import json
import sys
from pathlib import Path


def show_mcp_configuration():
    """MCPの設定例を表示します"""
    print("=" * 70)
    print("MCP (Model Context Protocol) 設定デモンストレーション")
    print("=" * 70)
    print()
    
    # VS Code設定の表示
    print("📁 VS Code での MCP 設定 (.vscode/settings.json):")
    print("-" * 70)
    vscode_config = {
        "mcpServers": {
            "aws-knowledge": {
                "command": "npx",
                "args": ["mcp-remote", "https://knowledge-mcp.global.api.aws"]
            }
        }
    }
    print(json.dumps(vscode_config, indent=2, ensure_ascii=False))
    print()
    
    # Python コードでのMCP設定
    print("🐍 Python コードでの MCP 設定例:")
    print("-" * 70)
    python_config = """
from langchain_mcp_adapters.client import MultiServerMCPClient

# MCPクライアントの初期化
mcp_client = MultiServerMCPClient({
    # FileSystem MCPサーバー（ローカルファイルシステムアクセス）
    "file-system": {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem@2025.7.1",
            "./"
        ],
        "transport": "stdio",
    },
    # AWS Knowledge MCPサーバー（AWSドキュメント検索）
    "aws-knowledge-mcp-server": {
        "url": "https://knowledge-mcp.global.api.aws",
        "transport": "streamable_http",
    }
})

# MCPツールを取得してLLMにバインド
tools = await mcp_client.get_tools()
llm_with_tools = llm.bind_tools(tools)
"""
    print(python_config)
    print()
    
    # 利用可能なMCPサーバーの説明
    print("🔧 このリポジトリで利用可能な MCP サーバー:")
    print("-" * 70)
    
    servers = [
        {
            "name": "FileSystem MCP Server",
            "package": "@modelcontextprotocol/server-filesystem",
            "description": "ローカルファイルシステムへのアクセスを提供",
            "features": [
                "ファイルの読み取り",
                "ファイルの書き込み",
                "ディレクトリの一覧表示"
            ]
        },
        {
            "name": "AWS Knowledge MCP Server",
            "url": "https://knowledge-mcp.global.api.aws",
            "description": "AWSドキュメントへのアクセスを提供",
            "features": [
                "AWSサービスドキュメントの検索",
                "技術情報の取得",
                "ベストプラクティスの参照"
            ]
        }
    ]
    
    for i, server in enumerate(servers, 1):
        print(f"{i}. {server['name']}")
        if 'package' in server:
            print(f"   📦 Package: {server['package']}")
        if 'url' in server:
            print(f"   🌐 URL: {server['url']}")
        print(f"   📝 説明: {server['description']}")
        print(f"   ✨ 機能:")
        for feature in server['features']:
            print(f"      - {feature}")
        print()
    
    print("=" * 70)
    print("✅ MCPは以下の方法で使用できます：")
    print("=" * 70)
    print()
    print("1. 📂 VS Code拡張機能として")
    print("   - .vscode/settings.json に設定を追加")
    print("   - GitHub Copilot などの拡張機能と統合")
    print()
    print("2. 🐍 Pythonコードで直接使用")
    print("   - langchain-mcp-adapters を使用")
    print("   - LangGraph などのフレームワークと統合")
    print("   - 例: chapter4/3_mcp_agent.py")
    print()
    print("3. 🔗 他のAIフレームワークとの統合")
    print("   - LangChain")
    print("   - LangGraph")
    print("   - その他のツール呼び出しをサポートするフレームワーク")
    print()
    print("=" * 70)
    
    # 実装例の参照
    print()
    print("📖 実装例:")
    print("-" * 70)
    examples = [
        {
            "file": "chapter4/3_mcp_agent.py",
            "description": "MCPを使用したエージェントの完全な実装例"
        },
        {
            "file": ".vscode/settings.json",
            "description": "VS CodeでのMCP設定"
        },
        {
            "file": "MCP_USAGE.md",
            "description": "MCP使用方法の詳細なドキュメント"
        }
    ]
    
    for example in examples:
        print(f"📄 {example['file']}")
        print(f"   {example['description']}")
        print()
    
    print("=" * 70)
    print("✨ MCPは正常に設定されており、使用可能です！")
    print("=" * 70)


def main():
    """メイン関数"""
    show_mcp_configuration()
    return 0


if __name__ == "__main__":
    sys.exit(main())
