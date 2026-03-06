# LLM Provider Configuration

Nanobot supports a wide variety of LLM providers. Here is how to configure the most common ones.

## 1. Anthropic (Claude)
The native choice for high-reasoning tasks.
```json
{
  "provider": "anthropic",
  "model": "claude-3-opus-20240229",
  "api_key": "your_api_key_here"
}
```

## 2. OpenRouter
The best choice for cost routing and accessing multiple models via a single API.
```json
{
  "provider": "openrouter",
  "model": "anthropic/claude-3-sonnet",
  "api_key": "your_openrouter_key"
}
```

## 3. DeepSeek
Excellent for coding tasks with high performance/cost ratio.
```json
{
  "provider": "deepseek",
  "model": "deepseek-coder",
  "api_key": "your_deepseek_key"
}
```

## 4. Local vLLM
For privacy-conscious or air-gapped deployments.
```json
{
  "provider": "openai_compatible",
  "base_url": "http://localhost:8000/v1",
  "model": "lmsys/vicuna-7b-v1.5",
  "api_key": "none"
}
```

## Switching Providers
You can switch providers on the fly by updating the `active_provider` field in your `config.json` or by using the `@Nanobot switch-provider` command.
