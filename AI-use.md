# A3 Recursive Patterns: AI use and academic integrity

Read this document before using AI for A3. These requirements apply alongside the program requirements in [brief.md](brief.md).

For this assignment, use only **the assignment guide extension** in VS Code. Do not use another model or AI service.

Read [brief.md](brief.md) for the program requirements, examples and testing instructions without the AI workflow and course policies.

## Starting your AI conversation

Use the assignment guide extension in VS Code for all your AI work on A3.

1. Read [brief.md](brief.md) and get the supplied starter files from the [repository](https://github.com/Alandougherty/comp1117_assignment_3_2026AB). Keep `assignment.json` in your assignment folder, unchanged. The extension reads it to load A3.
2. Install the Assignment Guide extension from the Visual Studio Code Marketplace. If you already have it, update it. A3 needs version 0.19.2 or later.
3. Open your assignment folder in VS Code. Keep the same folder for the whole assignment.
4. Open the Assignment Guide panel. Enter your course key if it asks. It is the same key as for A1. Use it for this course only, and do not share it.
5. Read the recording notice and agree to it. Nothing is sent until you do.

The assistant is set up as a tutor. It answers your questions, points out mistakes, and asks you what you think. It will write code for you once you have said what the code should do, in your own words. It will not write code you have not specified, and saying the rules back from the brief does not count as specifying them.

### Your chat history

The extension records every conversation on the course server, and your TA reads that record. If you start a new conversation in the extension, your earlier conversation stays in your record, and your TA can still read it.

**Export your chat history from the extension before you submit.** Export the whole chat, every message. The extension names the file `History.md` for you. Keep the name it gives you. Submit it complete and unedited, exactly as the extension exported it. Do not replace it with a summary or a reconstructed conversation. Follow the instructions posted on Ed for submitting it.

Every conversation about A3 must be with the assignment guide extension.


## How to work with the AI

**Work through this assignment with the AI assistant in the extension, in the following order.**

1. **Specify.** Work out the problem with the AI assistant: the inputs, the outputs, the rules for each function and the edge cases. Write them in `Specifications.md`, in your own words.
2. **Understand the logic.** Explain each part in your own words and trace what happens on small examples. Discuss anything you do not understand with the AI assistant.
3. **Build it together.** Work on one part at a time, writing code yourself or with the AI assistant's help. Review every suggestion and add your own comments explaining how the code works.
4. **Test it together.** Design your test cases in `tests.txt`. Work out each expected result by hand, and discuss your tests with the AI assistant to find the decisions you have not tested yet.

You submit four components: `Pattern.py` with your comments, `tests.txt`, `Specifications.md` and your exported chat history, `History.md`. There is no separate file for your logic. Explain each part in the chat before its code, and add your own comments explaining how it works and why. The marker reads both together. See the submission and grading sections below.


## What you submit

The supplied files are in the [assignment repository](https://github.com/Alandougherty/comp1117_assignment_3_2026AB). Keep their names.

| File | What it is | Who writes it |
|---|---|---|
| `README.md` | Starting page and links to the assignment documents | Supplied. Do not change it. |
| `brief.md` | Program requirements, examples and testing instructions | Supplied. Do not change it. |
| `AI-use.md` | AI workflow, conversation exports, grading and academic integrity policy | Supplied. Do not change it. |
| `assignment.json` | Identifies A3 for the assignment guide extension | Supplied. Do not change it. |
| `Pattern.py` | Your program, with your own comments explaining how each part works. **Use only the six supplied functions. Do not add functions, rename them or change their parameters**: the tests call them by name, so a renamed one counts as missing. `count_filled`, `fill_carpet` and `fill_tromino` must be recursive. | You, with the AI assistant; the comments by you |
| `Specifications.md` | The problem in your own words: inputs, outputs, the rules for each function and edge cases | You |
| `tests.txt` | Your function checks and program cases | You |
| `test.py` | Runs the worked examples and your tests | Supplied. Do not change it. |
| `History.md` | Your complete chat history, exported from the assignment guide extension | Exported, not edited |

Submit `Pattern.py`, `Specifications.md`, `tests.txt` and `History.md` to the A3 submission on Ed. Follow the instructions posted on Ed for submitting.


## How this is graded

| Component | Share | Marked by |
|---|---:|---|
| Code output | 35% | Automatic, against hidden test data |
| Your test cases | 35% | A teaching assistant, against a rubric |
| Your reasoning and use of AI | 30% | A teaching assistant, against a rubric |

Each component has four bands: Full, Substantial, Partial, and Weak / none. The mark for each band is fixed and shared with TAs.

**Code output, 35%.** Hidden program cases, as in A1 and A2, plus hidden checks that call your functions directly: `count_filled` and `find_quadrant` on their own, `fill_carpet` and `fill_tromino` on small grids and on regions that do not start at (0, 0), the value `fill_tromino` returns, and what `print_grid` prints and that it leaves the grid unchanged. So a correct part still earns marks even if another part has a mistake.

**Your test cases, 35%:**

| Level | What it looks like |
|---|---|
| Full | Your tests together cover **all** the decisions and boundaries the program must handle, each boundary from both sides, and all expected values are correct. Your function checks test `find_quadrant` on both sides of the row and column boundaries, including a region that does not start at (0, 0). Your program cases put the hole in all four quadrants, on a center cell and on an edge that is not a corner. |
| Substantial | Most decisions and boundaries are covered, with only a few gaps, and all expected values are correct. |
| Partial | Several decisions or boundaries are not covered, **or** one or more expected values are incorrect. |
| Weak / none | Very few tests and no meaningful coverage. No test file counts here. |

Expected values copied from a program that is wrong count as incorrect.

**Your reasoning and use of AI, 30%.** The marker reads `Specifications.md`, your chat history and the comments in `Pattern.py` together. Explanations in the chat before code and your own comments in the submitted code are both assessed; one does not replace the other. Write your explanations and answers in English, and write to the assignment guide in English only. English grammar is not assessed, but anything written in another language is not marked and earns nothing in this component. They look for:

- the rules specified in your own words, with both sides of each boundary, before any code;
- the logic of each part explained in the chat before that part's code, including how each recursive function reaches its base case and what each recursive call receives;
- your own comments in `Pattern.py` that explain how each part works;
- your own correct answers to the AI assistant's trace and predict questions, and how you corrected wrong ones;
- a real discussion of your test cases.

The marker judges the overall pattern across your work, not single messages. One good message does not earn a band, and one weak message does not lose it.

| Band | What the record shows across the assignment |
|---|---|
| **Full** | You specify the rules in your own words, with both sides of each boundary, before any code. You consistently explain each part in your own words before its code appears. Your questions are usually specific and build on what came before. You explain why each part works, trace and predict, correct mistakes, check what the AI assistant gives you, and say when you disagree. Your own comments explain why the code works. Your tests come out of a real discussion. |
| **Substantial** | Most of the time you explain before code and ask clear questions. But your explanations often stay close to the brief's wording, your checking is uneven, or your comments explain what the code does more than why. |
| **Partial** | Your own thinking appears now and then. Most of the record is requests for code or for the next step, and it is hard to see what you understood. Your own explanations and comments are limited. |
| **Weak / none** | Little of your own thinking is visible: the brief pasted in, repeated requests for code, or changes accepted without comment. Your own logic is hardly visible in the chat or code. |

If every part's logic came only from the AI assistant, every line of `Pattern.py` was suggested by it, and the code has no comments of your own, the mark for this component is Weak / none.

**What we are not grading:** whether your first answers were right. A wrong trace that you correct costs nothing. Being wrong and then noticing it is the exercise. You are also not marked on length: a short, precise exchange is better than a long one.

## Academic integrity

In A3, **the only AI tool you may use is the assignment guide extension**. Do not use any other AI tool for any part of this assignment: not ChatGPT, Copilot, Gemini, Claude.ai, an AI feature in your editor, or any other service. This covers your specification, your logic, your code, your tests, and your answers to the AI assistant's questions.

**Allowed:** discussing the problem with the AI assistant; asking it to explain a concept or a rule; having it review your code or help you with code for one part at a time; asking it which decisions your tests do not cover yet; reading the lecture notes and the textbook.

**Not allowed:**

- Using any AI tool other than the assignment guide extension, for any part of this assignment.
- Using another AI tool, a website or another person to answer the AI assistant's trace, predict or explain questions. Those answers must be yours. Submitting someone else's answer is submitting someone else's work.
- Sharing or copying chat histories, code, logic or test files with or from another student. Two submissions with the same chat history or the same test cases will both be treated as a violation. A public copy of your work on GitHub, or a fork of the assignment repository, counts as sharing.
- Submitting a conversation history that is not really yours, omitting assignment-related conversations, or editing, reconstructing or fabricating conversation content. Export your chat history from the extension and submit it complete and unedited, following the submission instructions on Ed.
- Changing `test.py`, `assignment.json`, the assignment brief, the function names and parameters in `Pattern.py`, or the output format.
- Attacking the AI assistant or the systems it runs on, including prompt injection, as set out in the next section.

### Attacking the AI assistant

**Using the assignment guide extension with the supplied `assignment.json` is permitted.** Asking the AI to clarify something, correct a mistake, explain differently or follow the requirements in the assignment brief is also permitted. These actions are not prompt injection.

**Not allowed:** any deliberate attempt to attack, subvert or misuse the AI assistant or the systems it runs on. That includes:

- prompt injection, as defined below;
- trying to make the AI assistant act outside this assignment: run a command, reach another system, service or account, or change a file, a repository or a setting outside your own assignment folder;
- trying to break into or disrupt the systems the AI assistant runs on by any route, whether through the AI assistant or directly;
- deliberately wasting or overloading the service, for example asking for output whose only purpose is to be as long as possible, or sending a run of messages that has nothing to do with the assignment;
- using another AI tool, a website or another person to write or improve prompts meant to do any of the above, or using prompts of that kind found elsewhere. Sending such a prompt counts the same as writing it yourself.

**What prompt injection means here.** Prompt injection is sending the AI assistant text that is meant to be obeyed as an instruction to the tool itself, rather than read as your message about the assignment, so that it ignores, replaces, reveals or works around the instructions the course gave it. Jailbreaking, which means trying to talk the AI assistant into doing what it was set up not to do, counts as prompt injection for this assignment. This includes deliberate attempts to bypass the course rules for permitted assistance.

**It does not matter how the text reaches the AI assistant.** It counts whether you:

- type or paste it into the chat;
- put it in a file the AI assistant reads, for example a comment in `Pattern.py`, a line in `Specifications.md`, a test case, or a changed `assignment.json`;
- disguise it as something else, such as a system or developer message, a role for the AI assistant to play, a template, a made-up transcript, or text hidden in characters that do not show on the screen.

**Some examples:** telling the AI assistant to ignore its previous instructions; telling it that it is no longer a tutor, or that the assignment rules no longer apply; asking it to print or reveal its instructions; pasting in text that claims to come from the course staff or from the system.

**It also covers text aimed at marking.** Anything in a file you submit that is meant to change how your work is marked, rather than to be part of your answer, is treated the same way.

**Attempting it is the violation.** Anything in this section is treated as a breach of academic integrity whether or not it works, and whether you wrote it yourself or got it from somewhere else. The test is what your message is for. A message about the Recursive Patterns program, the rules in the assignment brief or your own code is never an attack on the AI assistant, however firmly you put it. Arguing with the AI assistant about the program is part of the assignment.

The term prompt injection comes from computer security (see NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*). The definition above is the one this course applies.
