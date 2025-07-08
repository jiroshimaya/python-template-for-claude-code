---
title: CLAUDE.md
created_at: 2025-06-14
updated_at: 2025-07-08
# このプロパティは、Claude Codeが関連するドキュメントの更新を検知するために必要です。消去しないでください。
---

# Python開発テンプレート for Claude Code

厳格な型チェック、自動化されたコード品質管理、CI/CDを備えたPython 3.12+プロジェクトテンプレート。

## 技術スタック

**Python 3.12+** | uv | Ruff | mypy | pytest + Hypothesis | pre-commit | GitHub Actions

## プロジェクト構造(デフォルト。必要に応じて更新してください)


```
project-root/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── benchmark.yml
│   ├── dependabot.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── template/
│   ├── src/
│   │   └── template_package/    # モデルパッケージの完全な実装例
│   │       ├── __init__.py      # パッケージエクスポートの例
│   │       ├── py.typed         # 型情報マーカーの例
│   │       ├── types.py         # 型定義のベストプラクティス
│   │       ├── core/
│   │       │   └── example.py   # クラス・関数実装の模範例
│   │       └── utils/
│   │           ├── helpers.py   # ユーティリティ関数の実装例
│   │           ├── logging_config.py # ロギング設定の実装例
│   │           └── profiling.py # パフォーマンス測定の実装例
│   └── tests/                   # テストコードの完全な実装例
│       ├── unit/                # 単体テスト
│       ├── property/            # プロパティベーステスト
│       ├── integration/         # 結合テスト
│       └── conftest.py          # pytestフィクスチャ
├── src/                         # 実際の開発用ディレクトリ
│       └── project_name/
│           └── （プロジェクト固有のパッケージを配置）
├── tests/                       # 実際のテスト用ディレクトリ
│   ├── unit/
│   ├── property/
│   ├── integration/
│   └── conftest.py
├── docs/
├── scripts/
├── pyproject.toml
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
└── CLAUDE.md
```

## 実装時の必須要件

### 0. 開発環境
- Pythonコマンド: 必ず `uv run` を前置
- 依存関係追加: `uv add`
- GitHub操作: `make pr`/`make issue` または `gh`
- 品質チェック: `make check-all` を定期実行

### 1-5. 実装フロー
1. **コード品質**: make format → lint → typecheck → test
2. **テスト**: 新機能には必ずテスト作成（t-wada流TDD）
3. **ロギング**: 全コードにロギング実装必須
4. **パフォーマンス**: 重い処理はプロファイリング
5. **段階的実装**: 抽象クラス/Protocol定義 → テスト → 実装 → 最適化

### 6. エビデンスベース開発

**禁止語**: best, optimal, faster, always, never, perfect
**推奨語**: measured, documented, approximately, typically

**証拠要件**:
- パフォーマンス: "measured at Xms", "reduces by X%"
- 品質: "coverage X%", "complexity Y"
- セキュリティ: "scan detected X issues"
- 信頼性: "uptime X%", "error rate Y%"

### 7. 効率化テクニック

#### 実行パターン
- **並列処理**: 独立タスク同時実行
   - 例: 複数ファイルの読み込み、独立したテストの実行、並列ビルド
- **バッチ処理**: 類似操作をまとめて
   - 例: 複数ファイルのフォーマット、一括インポート修正、バッチテスト実行
- **逐次処理**: 依存関係順守
   - 例: - 例: データベースマイグレーション、段階的リファクタリング、依存パッケージインストール

#### エラーリカバリー
- **リトライ**: 最大3回、指数バックオフ
- **フォールバック**: 高速処理 → 確実な処理
- **状態復元**: チェックポイントからロールバック、最後の正常状態から再開、失敗した操作のみ再実行、代替アプローチの提案

#### 建設的フィードバックの提供

**フィードバックのトリガー**:
- 非効率なアプローチを検出
- セキュリティリスクを発見
- 過剰設計を認識
- 不適切な実践を確認

**アプローチ**:
- 直接的な表現 > 婉曲的な表現
- エビデンスベースの代替案 > 単なる批判
- 例: "より効率的な方法: X" | "セキュリティリスク: SQLインジェクション"

## template/ディレクトリの活用

実装前に必ず参照:
- **クラス/関数**
   - `template/src/template_package/core/example.py` で適切な型ヒント、docstring、エラーハンドリングを確認
   - `template/src/template_package/types.py` で型定義のパターンを確認
- **ユーティリティ**:
   - `template/src/template_package/utils/helpers.py` で関数の構造、エラー処理、ロギングを確認
- **テスト**:
   - `template/tests/unit/`: 単体テスト
   - `template/tests/property/`: プロパティベーステスト
   - `template/tests/integration/`: 結合テスト
   - `template/tests/conftest.py`: フィクスチャの実装例
- **ロギング**:
   - `template/src/template_package/utils/logging_config.py`
- 新しいコードを書く際は、まず`template/`内の類似例を確認しパターンを踏襲、プロジェクト固有の要件に合わせて調整
- `template/`は変更/削除せず、常に参照可能な状態を維持

## よく使うコマンド

```bash
# 基本
make help               # コマンド一覧
make check-all          # 全チェック実行
make clean              # キャッシュ削除

# 品質チェック
make format             # フォーマット
make lint               # リント
make typecheck          # 型チェック
make test               # テスト実行
make test-cov           # カバレッジ付きテスト

# GitHub操作
make pr TITLE="x" BODY="y" [LABEL="z"]     # PR作成
make issue TITLE="x" BODY="y"              # Issue作成

# 依存関係
uv add package_name               # 通常パッケージ
uv add --dev package_name         # 開発用パッケージ
```

## Git規則

**ブランチ**: feature/ | fix/ | refactor/ | docs/ | test/
**ラベル**: enhancement | bug | refactor | documentation | test

## コーディング規約

### ディレクトリ構成

パッケージとテストは `template/` 内の構造を踏襲、コアロジックは必ず `src/project_name` 内に配置

```
src/
├── project_name/
│   ├── core/
│   ├── utils/
│   ├── __init__.py
│   └── ...
├── tests/
│   ├── unit/
│   ├── property/
│   ├── integration/
│   └── conftest.py
├── docs/
...
```

### Python コーディングスタイル
- 型ヒント: Python 3.12+スタイル必須（mypy strict + PEP 695）
- Docstring: NumPy形式
- 命名: クラス(PascalCase)、関数(snake_case)、定数(UPPER_SNAKE)、プライベート(_prefix)
- ベストプラクティス: @template/src/template_package/types.py を参照

### エラーメッセージ

1. **具体的**: "Invalid input" → "Expected positive integer, got {count}"
2. **コンテキスト付き**: "Failed to process {source_file}: {e}"
3. **解決策を提示**: "Not found. Create by: python -m {__package__}.init"

### アンカーコメント
```python
# AIDEV-NOTE: 説明
# AIDEV-TODO: 課題
# AIDEV-QUESTION: 疑問
```

## テスト戦略（TDD）

t-wada流のテスト駆動開発（TDD）を徹底

### サイクル
🔴 Red → 🟢 Green → 🔵 Refactor

### 手順
1. TODOリスト作成
2. 失敗するテストを書く
3. 最小限の実装（仮実装OK）
4. リファクタリング

### 原則
- 小さなステップで進める
- 三角測量で一般化
- 不安な部分から着手
- テストリストを常に更新

#### 三角測量の例
```python
# 1. 仮実装: return 5
assert add(2, 3) == 5

# 2. 一般化: return a + b
assert add(10, 20) == 30

# 3. エッジケース確認
assert add(-1, -2) == -3
```

#### 注意点
- 1テストに複数の振る舞いを含めない
- Red→Greenでコミット
- 日本語テスト名推奨
- リファクタリング: 重複/可読性/SOLID違反時

### テスト種別
1. **単体テスト**: 基本動作（`template/tests/unit/`）
2. **プロパティベーステスト**: Hypothesis自動生成（`template/tests/property/`）
3. **統合テスト**: コンポーネント連携（`template/tests/integration/`）

### テスト命名
`test_[正常系|異常系|エッジケース]_条件で結果()`

## ロギング

### 必須要件
1. モジュール冒頭でロガー定義
2. 関数開始/終了時にログ出力
3. エラー時: `exc_info=True`
4. レベル: DEBUG(詳細)/INFO(重要)/WARNING(注意)/ERROR(エラー)

ベストプラクティス:
- @template/src/template_package/utils/logging_config.py
- @template/src/template_package/core/example.py

### 設定
```python
setup_logging(level="INFO")
# または export LOG_LEVEL=INFO
```

## パフォーマンス測定

```python
from template_package.utils.profiling import profile, timeit, Timer

@profile  # 詳細プロファイル
@timeit   # 実行時間計測
def func(): ...

with Timer("operation"):  # ブロック計測
    ...
```

ベストプラクティス:
- @template/src/template_package/utils/profiling.py

## 更新トリガー

- 仕様/依存関係/構造/規約の変更時
- 同一質問2回以上 → FAQ追加
- エラーパターン2回以上 → トラブルシューティング追加

## トラブルシューティング/FAQ

適宜更新

## カスタムガイド

`docs/`に追加可能。追加時はCLAUDE.mdに概要記載必須。
