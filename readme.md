# AgentShield

## Multi-Agent AI Firewall for Cross-Language Prompt Injection Detection

---

### What is AgentShield?

AgentShield is a **multi-agent firewall** that protects AI agents from prompt injection attacks across languages. Instead of relying on a single model — which always has blind spots — AgentShield deploys **multiple specialized detection agents** that cross-validate every incoming prompt before it reaches your AI system.

One line: **We use AI agents to protect AI agents.**

---

### The Problem

Prompt injection is the #1 security vulnerability in AI agent deployments. Attackers embed hidden instructions in user inputs to hijack agent behavior, steal data, or bypass safety guardrails.

Current defenses have a critical flaw: **they only work in English.**

- Meta's Prompt-Guard-2: Chinese attack detection rate < 40%
- LlamaFirewall: Minimal CJK language support
- Rule-based filters: Trivially bypassed with homophone substitution, mixed-language injection, or encoding tricks

China is the world's second-largest AI market. Every enterprise serving Chinese-speaking users is running AI agents with no effective security layer.

---

### The Solution: Multi-Agent Ensemble Detection

AgentShield's firewall is itself a multi-agent system, built on our proprietary **ANG™ (Agentic Neural Graph)** protocol:

```
User Prompt
    │
    ▼
┌─────────────────┐
│  Router Agent    │  Language detection & classification
│  (Agent 1)       │  Determines routing strategy
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌────────┐
│ Gemini │ │  Qwen  │  Parallel detection
│ Agent  │ │  Agent │  Specialized per language
│(Agent 2)│ │(Agent 3)│
└───┬────┘ └───┬────┘
    │          │
    ▼          ▼
┌─────────────────┐
│  Fusion Agent   │  Cross-validation & conflict arbitration
│  (Agent 4)       │  Final threat verdict + confidence score
└─────────────────┘
         │
         ▼
   SAFE / SUSPICIOUS / MALICIOUS
```

**Agent 1 — Router Agent**
Receives the incoming prompt, performs language detection and preliminary classification, and decides which detection agents to activate and with what priority.

**Agent 2 — Gemini Detection Agent** (Google AI Studio)
General-purpose attack pattern recognition. Optimized for English-language jailbreaks, data exfiltration attempts, role hijacking, and privilege escalation.

**Agent 3 — Qwen Detection Agent** (MegaNova self-hosted, Qwen3-Plus)
Chinese-specialized deep detection. Handles Simplified/Traditional混用 bypass, homophone substitution (谐音绕过), instructions embedded in translation tasks, mixed EN/ZH injection, and Unicode variant attacks.

**Agent 4 — Fusion Agent**
Collects results from all detection agents, performs conflict arbitration. If agents disagree, it escalates the threat level and flags the divergence. Outputs final verdict with composite confidence score.

---

### Detection Capabilities

**General Attacks (Gemini Engine)**
- Jailbreak / DAN-style attacks
- Data exfiltration (e.g., "send user data to external server")
- Role hijacking ("you are now an unrestricted AI")
- Privilege escalation ("admin override", "system command")
- Social engineering manipulation

**Chinese-Specialized Attacks (Qwen Engine)**
- 繁简混用 bypass (Simplified/Traditional Chinese mixing)
- 谐音替换 (Homophone substitution to evade keyword filters)
- 翻译任务注入 (Malicious instructions hidden inside translation requests)
- 中英混合注入 (Mixed EN/ZH injection patterns)
- Unicode变体攻击 (Unicode variant character attacks)
- 角色劫持 (Chinese-language role hijacking)

---

### Why Multi-Agent?

No single model can catch everything. Each model has language-specific and pattern-specific blind spots:

| Scenario | Single-Model Firewall | AgentShield (Multi-Agent) |
|---|---|---|
| English jailbreak | ✓ Detected | ✓ Detected by Gemini Agent |
| Chinese role hijacking | ✗ Missed | ✓ Detected by Qwen Agent |
| Mixed EN/ZH injection | ✗ Missed | ✓ Cross-validated by both agents |
| Novel attack pattern | ✗ Unknown | ⚠ Flagged via agent disagreement |

When detection agents disagree, that disagreement itself is a signal. The Fusion Agent treats divergence as elevated risk — a capability impossible with single-model approaches.

---

### Powered by ANG™

AgentShield is the first production application of **ANG™ (Agentic Neural Graph)**, our proprietary multi-agent orchestration protocol. ANG™ enables self-organizing agent networks where specialized agents collaborate on complex tasks without rigid, pre-defined workflows.

AgentShield proves the protocol: a multi-agent system that protects other people's agents, built and orchestrated by our own framework.

---

### Tech Stack

| Layer | Technology |
|---|---|
| Detection Engine 1 | Gemini 2.0 Flash (Google AI Studio, free tier) |
| Detection Engine 2 | Qwen3-Plus (MegaNova platform, self-hosted) |
| Orchestration | ANG™ (Agentic Neural Graph) protocol |
| Demo Deployment | Google Cloud Run |
| Production Infra | Nebula Block GPU cluster (Canada) |

---

### Market Opportunity

- **TAM**: $8.5B+ AI security market by 2028 (Gartner)
- **Beachhead**: GPU cloud providers, AI agent platforms, enterprises with multilingual AI deployments
- **Business model**: API usage-based pricing ($0.001/scan), enterprise tier with private deployment and custom detection agents
- **Expansion**: Add Japanese, Korean, Arabic detection agents as the ensemble grows

---

### Why Us — Not a Hackathon Toy

**Nebula Block** — Canadian sovereign GPU cloud. SOC 2 complete, ISO 27001 in progress. We run our own infrastructure and deploy our own models at cost.

**MegaNova + ANG™** — Production AI agent platform with proprietary multi-agent orchestration. Qwen3-Plus runs on our own GPUs.

**Battle-tested** — We survived a real supply-chain attack (axios@1.14.1 compromise, C2 server identified, March 2025). Security is not a feature for us. It's a survival requirement.

**Team** — CEO & technical founder with 15+ years at IBM, SAP, Autodesk, Expedia. Previous exit (EqualDocs). Founded Swan Chain (backed by Binance Labs, Optimism grants).

---

### Contact

- **Web**: nebulablock.com | meganova.ai
- **GitHub**: github.com/flyworker
