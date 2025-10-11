# README

欢迎 AFT 的大家来到首届算子挑战赛！

## Overview

* 算子比赛通过 Github 的 Action 机制模拟了一个非常简易 Online Judge 平台，每周这里会切换一个 Task，每个 Task 就是不同的算子，例如第一周将会是实现高效的 `rolling_rank()`
* 评分的 Action 需要通过提交 PR 来触发，所以这也是一个熟悉 Git/Github 的一个机会
* 由于初次尝试，系统非常可能具有极大的不稳定性，如遇 bug 请反馈给会长，相信通过大家不断的使用，系统会快速迭代起来
* 任何问题都可以随意提 issue

## Build ops

* 在 `src/solution.py` 是参考的基础 pandas 写法，需要完成读取+计算两个步骤
    * 注意只需要完成 `ops_rolling_rank()` 函数，且函数签名是 `(input_path: str, window: int = 20)`
    * 用于测试的 `main` 逻辑自行完成，提交时请只保留函数
* 测试数据可以从 [北大网盘]() 获取，需要校园网

## Submit PR

1. 点击 fork 将仓库到自己的 Github 下
2. 建立一个新分支，例如 `git checkout -b week1`
3. 从 [北大网盘]() 下载 Testcase，在本地修改并测试 `src/solution.py` 后 push 回本地
4. 在你的本地仓库提交 PR
5. 注意尽量不要提交太多次，后端的 LeaderBoard 可能只会计算前三次的成绩

