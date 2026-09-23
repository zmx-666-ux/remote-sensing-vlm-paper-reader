# 遥感 VLM 论文精读助手

[English](README.md)

这是一个面向遥感视觉语言模型（VLM）与多模态变化检测研究者的 Codex Plugin。它帮助你精读论文、保留页码证据，并持续维护会随新论文修正的研究知识库。

## 适用范围

本 Skill 刻意限定于遥感 VLM、双时相视觉—语言推理、变化描述、语义变化检测及其紧密相关的多模态变化检测研究，不是通用 PDF 摘要器。

支持五种阅读模式：

1. 快速筛选；
2. 新手精读；
3. 复现分析；
4. 创新分析；
5. 跨论文对比。

## 主要产物

- 使用 [`paper-note-template.docx`](skills/remote-sensing-vlm-paper-reader/assets/paper-note-template.docx) 生成十二部分的 Word 精读笔记。
- 使用 [`research-ledger-template.xlsx`](skills/remote-sensing-vlm-paper-reader/assets/research-ledger-template.xlsx) 维护六张可见工作表组成的 Excel 研究台账。
- 明确区分“作者主张”“证据支持范围”和“分析/推断”。
- 对方法、图表、公式、结果与局限保留 PDF 页码证据。
- 新论文出现后更新创新点和模块的状态，不删除旧判断，保留研究演化过程。

可先查看不含真实论文内容的[虚构示例](examples/synthetic-example/example-request.md)。

## 快速开始

1. 按[安装指南](docs/installation.md)完成安装，然后重启 Codex。
2. 将论文 PDF、生成的笔记和已填写台账放在本仓库之外的私人文献库。
3. 可以直接这样发起任务：

   > 对这个本地 PDF 使用新手精读模式。假设我有图像处理基础但不了解 VLM；先讲前置知识，保留 PDF 页码证据，生成十二部分笔记，并提出有证据的研究台账更新。

[Paper Pilot](docs/paper-pilot-setup.md) 是可选且由独立项目维护的增强组件。可用时，它能辅助检索、下载、连续阅读全文和查看关键页；不可用时，本 Skill 会读取你提供的 local PDF，并明确说明没有执行在线检索。

## 隐私与证据规则

本仓库只保存可复用的指令、空白模板和虚构示例。请勿把私人 PDF、精读笔记、未公开创新点、个人路径、凭据或已填写的台账放进 Plugin 仓库。自动隐私测试会阻止 PDF 和已知私人标记进入待发布文件。

只有摘要不能视为完成全文精读。缺失信息必须写成“未找到”“论文未报告”或“需要代码验证”，不能猜测；长段原文应改为释义并保留页码。

## 已知限制

- 在线检索与下载取决于 Paper Pilot、网络以及论文是否可访问。
- 扫描版 PDF 可能需要先做 OCR，才能可靠地按页取证。
- 单篇论文不能证明一个想法具备新颖性，还需要单独查新和可比证据。
- Word 与 Excel 生成能力取决于当前 Codex 环境可用的文档工具。

## 参与改进

提交 issue 时请提供最小化的虚构示例、预期行为和实际行为，不要上传私人研究材料。修改工作流时，应继续保留稳定 ID、证据链接和历史状态变化。

详细说明见[安装指南](docs/installation.md)与[Paper Pilot 配置](docs/paper-pilot-setup.md)。

本项目采用 [MIT License](LICENSE)。
