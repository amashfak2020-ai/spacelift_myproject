# 🚀 Spacelift My Project

A cloud infrastructure automation project managed and deployed via [Spacelift](https://spacelift.io/) — the smart CI/CD platform for infrastructure-as-code.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Spacelift Setup](#spacelift-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 Overview

`spacelift_myproject` is a repository designed to manage infrastructure deployments using Spacelift. Spacelift is a sophisticated, policy-as-code powered CI/CD platform for infrastructure-as-code tools such as Terraform, OpenTofu, Pulumi, Ansible, and CloudFormation.

This project demonstrates how to:
- Define and manage infrastructure as code
- Automate deployments through Spacelift stacks
- Enforce policies and approval workflows
- Track and audit infrastructure changes

---

## ✨ Features

- 🏗️ **Infrastructure as Code** — Declarative infrastructure definitions for repeatable, version-controlled deployments
- 🔄 **Automated CI/CD** — Triggered runs on every push through Spacelift
- 🔐 **Policy Enforcement** — Plan, access, and approval policies to safeguard deployments
- 🌍 **Multi-Environment Support** — Manage dev, staging, and production environments with ease
- 📊 **Audit Trails** — Full visibility into all infrastructure changes and who made them
- 🔔 **Notifications** — Integrated alerts for plan and apply events

---

## 🛠️ Prerequisites

Before getting started, ensure you have the following installed and configured:

| Tool | Version | Purpose |
|------|---------|---------|
| [Terraform](https://www.terraform.io/) / [OpenTofu](https://opentofu.org/) | Latest | Infrastructure provisioning |
| [Git](https://git-scm.com/) | 2.x+ | Version control |
| [Spacelift Account](https://spacelift.io/) | — | CI/CD orchestration |
| Cloud Provider CLI (AWS/GCP/Azure) | Latest | Cloud authentication |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/amashfak2020-ai/spacelift_myproject.git
cd spacelift_myproject
```

### 2. Configure Cloud Credentials

Set up your cloud provider credentials. For example, with AWS:

```bash
export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
export AWS_DEFAULT_REGION="us-east-1"
```

### 3. Initialize the Project

```bash
terraform init
```

### 4. Plan Infrastructure Changes

```bash
terraform plan
```

### 5. Apply Changes

```bash
terraform apply
```

> **Note:** In a Spacelift-managed workflow, the plan and apply steps are automatically triggered via Spacelift stacks upon pull requests or direct pushes.

---

## 📁 Project Structure

```
spacelift_myproject/
├── demo                  # Demo/sample file
├── .spacelift/           # Spacelift configuration (if applicable)
├── modules/              # Reusable Terraform modules
├── environments/         # Per-environment variable files
│   ├── dev/
│   ├── staging/
│   └── prod/
├── policies/             # Spacelift OPA policies
├── main.tf               # Root Terraform configuration
├── variables.tf          # Input variable definitions
├── outputs.tf            # Output value definitions
├── versions.tf           # Provider and Terraform version constraints
└── README.md             # Project documentation
```

---

## ☁️ Spacelift Setup

### Creating a Stack

1. Log in to your [Spacelift account](https://app.spacelift.io/).
2. Click **Create Stack**.
3. Connect it to this GitHub repository: `amashfak2020-ai/spacelift_myproject`.
4. Select your IaC tool (e.g., Terraform/OpenTofu).
5. Set the project root directory if needed.
6. Configure your environment variables and cloud credentials as Spacelift contexts.

### Triggering Runs

- **On Push:** A tracked push to the `main` branch triggers a planned and auto-applied run.
- **On Pull Request:** A pull request triggers a speculative plan for preview without applying changes.
- **Manual Run:** Trigger runs manually from the Spacelift UI or via the API.

### Policies (Optional)

Spacelift supports [OPA (Open Policy Agent)](https://www.openpolicyagent.org/) policies for:

```rego
# Example: Require approval for production deployments
package spacelift

deny[sprintf("Production deployments require approval: %s", [resource.address])] {
  input.run.stack.id == "production"
  not input.run.user_provided_metadata.approved
}
```

---

## 🔧 Usage

### Local Development

Make infrastructure changes locally, review the plan, and push to GitHub:

```bash
# Make your changes, then:
git add .
git commit -m "feat: add new resource"
git push origin feature/my-change
```

Spacelift will automatically detect the push and trigger a speculative plan.

### Merging to Main

Once a pull request is reviewed and merged into `main`, Spacelift will:
1. Run a full `terraform plan`
2. (Optionally) Wait for approval
3. Execute `terraform apply`

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'feat: add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Commit Message Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Usage |
|--------|-------|
| `feat:` | New feature or resource |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code refactoring |
| `chore:` | Maintenance tasks |

---

## 📄 License

This project is open source. Please add a license file (e.g., MIT, Apache 2.0) as appropriate for your use case.

---

## 📬 Contact

**Ashfak A Mohammad**

- GitHub: [@amashfak2020-ai](https://github.com/amashfak2020-ai)
- Email: amashfak2020@gmail.com

---

## 🔗 Useful Links

- [Spacelift Documentation](https://docs.spacelift.io/)
- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [OpenTofu Documentation](https://opentofu.org/docs/)
- [OPA Policy Reference](https://docs.spacelift.io/concepts/policy)

---

> ⭐ If you find this project useful, please consider giving it a star!
