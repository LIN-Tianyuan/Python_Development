# Git
##  1. Git Branching

------

### **✅ Git branching basics**

```bash
# Create a new branch and switch to it
git checkout -b feature-branch

# Switch back to the main branch
git checkout main

# Merge branch
git merge feature-branch

# Delete branch
git branch -d feature-branch

# Deleting a remote branch
git push origin --delete feature-branch
```

📌 **Key point**

- `git checkout -b` → create and switch branches
- `git merge` → merge branches
- `git branch -d` → delete local branch
- `git push origin --delete` → Delete a remote branch.

------

### **✅ Git Flow Workflow**

**The Git Flow Branching Model**

```bash
main <------ official online branch
│
├── develop <------ development branch
│ ├─ feature/xxx <------ feature branch
│ ├─ feature/yyyy
│
├─ release/1.0.0 <------ pre-release branch
│
├── hotfix/bugfix <------ online emergency fixes
```

✅ **Git Flow suitable for** large teams, multi-environment development

✅ **GitHub Flow for** CI/CD, direct `main` development + PR

## **2. Resolve Merge Conflicts**

------

### **✅ Example of a Git merge conflict**

```bash
git merge feature-branch
```

🚨 **If there is a conflict, Git will prompt**

```pgsql
CONFLICT (content): Merge conflict in example.txt
```

👨‍💻 **Resolution**

1. **Open the conflicting file** (`example.txt`)
2. **Modify the conflict manually**

```diff
<<<<<<< HEAD
Modifications to version A
=======
Modifications to version B
>>>>>>> feature-branch
```

3. **Remove conflicting flags, retain correct code**

```diff
Changes to Version B # Manual retention of final code
```
4. **Submission of amendments**

```bash
git add example.txt
git commit -m "Resolve merger conflicts"
git push
```

------

### **✅ Rebase vs Merge**

```
git checkout feature-branch
git rebase main
```

📌 **DISTINCTIONS**

| Operations | Scenarios | Impacts |
| -------- | ------------------ | --------------------------------------- |
| `merge` | For normal merges | **Preserve branch history** (redundant merge commits) |
| `rebase` | for keeping linear history | **make branch history cleaner** |

🚀 **Best practices**:

- `rebase` for **feature branching to synchronize master branches**.
- `merge` for **feature branches that eventually merge into `main`**.

## **3. PR (Pull Request) Code review**

------

A **Pull Request (PR, pull request)** is a **code merge mechanism** provided by **Git platforms (e.g., Bitbucket, GitHub, GitLab)** to allow developers **to commit changes before merging the code and to allow team members to perform a Code Review**.
### **✅ PR code review best practices**

| **Best Practices** | **Interpretation** |
| --------------------- | ------------------------------------------------ |
| **Small and clear PR** | Avoid huge PRs, suggest **One task per PR** |
| **Describe clearly** | Title and description of the PR should be clear, explain **why this change was made** |
| **Include Tests** | Code changes should have corresponding **test cases** |
| **Follow the code style** |**Code should be formatted consistently and conform to the team's**code specification|
| **Avoid `force pushes`** | **Don't `force push`** unless you specifically need to `force push`|
------

### **✅ Create Pull Request（PR）**

**📌 Bitbucket Or GitHub**

1. `git push origin feature-branch`
2. Create a Pull Request at **Bitbucket/GitHub**.
3. Have a coworker **Review and merge** the request.

------

### **✅ Request Changes in PR**

If there is a problem with the code, **Review can “Request Changes ”**:

- **Formatting issue**: 💡 `“Variable naming is not clear, suggest to change to user_id”`
- **Performance Optimization**: 🚀 `“Unnecessary SQL query in loop, suggest to optimize it”`
- **Security issue**: 🔐 `“SQL injection risk in SQL splicing, suggest using parameterized queries”`

📌 **A good PR review should**: 
 - ✅ Point out problems
 - ✅ Give **Optimization suggestions**
 - ✅ Explain **why it was changed**

How do we resolve Git merge conflicts?

 - **When Git has a merge conflict, we run `git status` to find the conflict file**. Then we manually edit the file, remove the `<<<< HEAD` tag, select the correct code version, and finally `git add` and commit the changes.

 - In teamwork, we usually **avoid** leaving `main` unmerged for long periods of time, and `rebase` periodically to minimize conflicts.

How does the team conduct PR code reviews?

 - On our team, we use **Bitbucket PRs** for code reviews, and our best practices are:

1. **PRs are small and clear**, with each PR containing only **one feature change**.
2. **Review focuses on code quality**, including performance optimizations, error handling, and security.
3. **Use automated tests** and all PRs must pass CI/CD tests.
4. **Avoid `force pushes`** to ensure a clean and traceable code history.