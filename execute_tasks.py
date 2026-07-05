import os
import subprocess

REPO_DIR = r"C:\Users\ishan\Documents\Projects\Awesome-Constitutional-AI"

def run_git(commit_msg):
    cmd = f"cd Awesome-Constitutional-AI; git add .; git commit -m '{commit_msg}'; git push"
    print(f"Executing: {cmd}")
    result = subprocess.run(["powershell", "-Command", cmd], cwd=os.path.dirname(REPO_DIR), capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git execution failed: {result.stderr}\n{result.stdout}")
    else:
        print(f"Success: {result.stdout}")

os.makedirs(os.path.join(REPO_DIR, "pages"), exist_ok=True)
os.makedirs(os.path.join(REPO_DIR, "assets"), exist_ok=True)

pages_data = [
    ("The Manual Crowdsourced Alignment Era (Traditional RLHF)", "Traditional_RLHF.md", "Traditional RLHF uses human preference data to train reward models. \n\n```mermaid\ngraph TD;\n    A[Model] --> B[Human Annotator];\n    B --> C[Reward Model];\n    C --> D[PPO Update];\n```"),
    ("The Principle-Guided Feedback Revolution (Constitutional AI / RLAIF)", "Constitutional_AI.md", "Constitutional AI replaces human preference with AI feedback guided by a Constitution.\n\n```mermaid\ngraph LR;\n    A[Toxic Prompt] --> B[Critique vs Constitution] --> C[Safe Revision];\n```"),
    ("The Internalized Thinking & Self-Correction Era", "Self_Correction.md", "Models use systemic reasoning to verify safety natively.\n\n```mermaid\ngraph TD;\n    A[Prompt] --> B[Hidden CoT];\n    B --> C{Check Rules};\n    C -- Pass --> D[Output];\n    C -- Fail --> B;\n```"),
    ("The Monosemantic Dictionary Steering Enclave Era", "Steering_Enclave.md", "Sparse Autoencoders and Steering Vectors clamp concepts directly.\n\n```mermaid\ngraph TD;\n    A[Activations] --> B[SAE];\n    B --> C[Clamp features] --> D[Output];\n```"),
    ("A. Supervised Constitutional AI (Critique-Revision SFT)", "Supervised_CAI.md", "The supervised fine-tuning phase of Constitutional AI.\n\n```mermaid\ngraph LR;\n    A[Generation] --> B[Self-Critique] --> C[Revision];\n```"),
    ("B. Reinforcement Learning from AI Feedback (RLAIF Preference Modeling)", "RLAIF_Preference.md", "AI scores pairwise completions to train a Reward Model.\n\n```mermaid\ngraph TD;\n    A[Response 1 & 2] --> C[AI Evaluator] --> D[RM Training];\n```"),
    ("C. Direct Constitutional Preference Optimization (Constitutional DPO)", "Constitutional_DPO.md", "Eliminates RM by directly optimizing LM using DPO.\n\n```mermaid\ngraph TD;\n    A[AI Feedback] --> B[Logit Deltas] --> C[DPO Loss];\n```"),
    ("D. Multi-Constitutional Hypernetworks", "Hypernetworks.md", "A conditioning network controls parameters dynamically.\n\n```mermaid\ngraph LR;\n    A[Conditioning Vector] --> B[Hypernetwork] --> C[Main LM];\n```"),
    ("Constitutional Prompt Registries", "Prompt_Registries.md", "Immutable library of explicit textual rules to guide evaluations.\n\n```mermaid\ngraph TD;\n    A[Rule 1] & B[Rule 2] --> C[Registry] --> D[Eval Injection];\n```"),
    ("Logit Divergence Accountants", "Logit_Divergence.md", "KL Divergence penalty keeps the model from mode collapse.\n\n```mermaid\ngraph TD;\n    A[Active Logits] & B[Ref Logits] --> C[KL Penalty];\n```"),
    ("The Over-Alignment Capability Drain (The Refusal Stagnation Tax)", "Capability_Drain.md", "Strict rules cause refusal underfitting (false positives).\n\n```mermaid\ngraph TD;\n    A[Benign Query] --> B[Over-aligned Filter] --> C[Refusal];\n```"),
    ("The Reward Hacking and Critique Blindness Trap", "Critique_Blindness.md", "Confirmation bias if same model generates and critiques.\n\n```mermaid\ngraph LR;\n    A[Flawed Generation] --> B[Same Evaluator] --> C[False Reinforcement];\n```"),
    ("Enterprise Chatbot Persona & Guardrail Standardization (Claude/Llama Systems)", "Enterprise_Chatbot.md", "Standardization ensures commercial assistants follow laws.\n\n```mermaid\ngraph TD;\n    A[Base Model] --> B[Constitutional FT] --> C[Compliant Assistant];\n```"),
    ("Automated Cyber-Security Red-Teaming & Exploit Screening", "Cyber_Security.md", "Autonomous constitutional critics block exploits.\n\n```mermaid\ngraph TD;\n    A[Tool Intent] --> B[Monitor] -- Exploit --> C[Block];\n```"),
    ("Sovereign Legal & Financial Portfolio Compliance Auditing", "Compliance_Auditing.md", "Custom corporate constitutions for parsing tax and legal data.\n\n```mermaid\ngraph TD;\n    A[Legal Data] --> B[Constitution Auditor] --> C[Variance Report];\n```"),
]

readme_path = os.path.join(REPO_DIR, "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

for title, filename, content in pages_data:
    page_path = os.path.join(REPO_DIR, "pages", filename)
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content}\n")
    
    target = f"**{title}**"
    replacement = f"**[{title}](pages/{filename})**"
    readme_content = readme_content.replace(target, replacement)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("detailed pages created")

svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(20,20,50);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(80,20,100);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" rx="15" ry="15"/>
  <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="40" fill="white" font-weight="bold" text-anchor="middle" dominant-baseline="middle">Awesome Constitutional AI</text>
  <text x="50%" y="70%" font-family="Arial, sans-serif" font-size="20" fill="#ddd" text-anchor="middle" dominant-baseline="middle">Alignment, Security &amp; Steering Vectors</text>
  <circle cx="50" cy="50" r="20" fill="white" opacity="0.2">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="750" cy="150" r="20" fill="white" opacity="0.2">
    <animate attributeName="r" values="20;30;20" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>'''

with open(os.path.join(REPO_DIR, "assets", "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_banner)

readme_content = readme_content.replace("# Awesome-Constitutional-AI", "# 🚀 Awesome-Constitutional-AI\n\n![Banner](assets/banner.svg)")
readme_content = readme_content.replace("## Constitutional AI: History, Progression, Variants, & Applications", "## 📜 Constitutional AI: History, Progression, Variants, & Applications")
readme_content = readme_content.replace("## 1. The Macro Chronological Evolution", "## 🕰️ 1. The Macro Chronological Evolution")
readme_content = readme_content.replace("## 2. Core Functional & Algorithmic Variants", "## ⚙️ 2. Core Functional & Algorithmic Variants")
readme_content = readme_content.replace("## 3. The Constitutional AI Generation Pipeline", "## 🏭 3. The Constitutional AI Generation Pipeline")
readme_content = readme_content.replace("## 4. Production Engineering Challenges & Mitigations", "## ⚠️ 4. Production Engineering Challenges & Mitigations")
readme_content = readme_content.replace("## 5. Frontier Real-World AI Infrastructure Applications", "## 🌍 5. Frontier Real-World AI Infrastructure Applications")
readme_content = readme_content.replace("## References", "## 📚 References")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("added emojis and banner")

seo_meta = '''<!-- SEO Optimization -->
<meta name="description" content="A curated list of awesome Constitutional AI resources, papers, architectures, and variants including RLAIF, DPO, and SAEs.">
<meta name="keywords" content="Constitutional AI, RLAIF, AI Alignment, AI Safety, Machine Learning, Deep Learning, Sparse Autoencoders">
'''

left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

target_banner = "![Banner](assets/banner.svg)\n"
readme_content = readme_content.replace(target_banner, f"{target_banner}\n{seo_meta}\n<div align=\"center\">\n{left_badges}\n</div>\n\n")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("seo optimised and badges to left added")

right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
readme_content = readme_content.replace(left_badges, f"{left_badges}\n{right_badge}")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("badges to right added")

star_history = '''
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Constitutional-AI&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Constitutional-AI&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Constitutional-AI&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Constitutional-AI&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''

readme_content += f"\n{star_history}"
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("star history added")

readme_content = readme_content.replace("chartrepos", "chart?repos")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("fixed star plot")

readme_content = readme_content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

run_git("invalid awesome link fixed")

print("Python script execution finished.")
