# Research-ledger schema

`文献研究台账.xlsx` is the structured source of truth for evolving knowledge. Keep six visible worksheets and one hidden `_配置` worksheet for validation lists. Freeze row 1, enable filters, wrap long text, and use stable IDs rather than titles as relationships.

## 论文索引

Columns: `论文ID`, `PDF文件名`, `完整标题`, `年份`, `期刊会议`, `DOI_arXiv`, `代码地址`, `数据集地址`, `研究任务`, `模态`, `方法标签`, `阅读优先级`, `阅读状态`, `精读笔记路径`, `一句话结论`, `主要贡献`, `关键局限`, `最后阅读日期`, `最后核查日期`.

Reading statuses: `待读`, `阅读中`, `已精读`, `需复读`, `仅作参考`. Priorities: `高`, `中`, `低`.

## 创新假设

Columns: `创新ID`, `问题`, `假设摘要`, `灵感来源论文`, `最接近已有工作`, `预期新颖性`, `与已有工作差异`, `所需数据`, `所需算力`, `所需标注`, `实现条件`, `最小验证实验`, `成功判据`, `主要风险`, `当前状态`, `置信度`, `覆盖或否定论文`, `下一步行动`, `最后更新时间`.

Statuses: `初始想法`, `待查新`, `候选`, `值得实验`, `实验中`, `已采用`, `被已有工作覆盖`, `证据不足`, `已否定`, `已归档`.

## 模块方法库

Columns: `模块ID`, `模块方法名称`, `所属论文`, `流程位置`, `输入`, `输出`, `核心计算`, `设计动机`, `解决问题`, `论文证据`, `适用条件`, `缺点`, `失败场景`, `计算量`, `显存要求`, `开源代码`, `可替代模块`, `后继改进`, `当前状态`, `最后更新时间`.

Statuses: `待评估`, `有参考价值`, `准备复现`, `复现中`, `已验证`, `效果存疑`, `被替代`, `不适用`, `已归档`.

## 跨论文对比

Columns: `论文ID`, `任务定义`, `视觉编码器`, `文本编码器`, `跨模态对齐`, `时相交互`, `融合位置`, `解码方式`, `训练阶段`, `损失函数`, `数据集`, `指标`, `参数量`, `算力`, `代码开放性`, `主要优势`, `主要局限`, `可比性备注`.

## 概念术语

Columns: `术语ID`, `中文术语`, `英文术语`, `通俗解释`, `技术定义`, `相关概念`, `代表性论文`, `掌握状态`, `最后更新时间`.

## 待读问题

Columns: `问题ID`, `问题`, `来源论文`, `需要验证的判断`, `验证方式`, `处理状态`, `关联创新ID`, `关联模块ID`, `最后更新时间`.

## Write contract

- On first use, ask for the private research-library root and store relative artifact paths when possible.
- Before assigning an ID, scan existing IDs and choose the next number without reusing archived IDs.
- Update an existing row when the identity matches; do not create duplicates to avoid resolving a conflict.
- If the workbook is locked or its schema differs materially, stop and report the path and mismatch.
- Ordinary inspirations remain ledger rows. Create a separate innovation Word only after status reaches `值得实验`; create an experiment Word only after a module reaches `准备复现` or `复现中`.
