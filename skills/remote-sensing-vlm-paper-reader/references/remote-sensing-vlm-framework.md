# Remote-sensing VLM and multimodal change-detection framework

Use these dimensions to locate a paper and compare it fairly. Do not require every paper to fill every dimension.

## Problem taxonomy

| Family | Typical input | Typical output | Main distinction |
|---|---|---|---|
| Binary change detection | bi-temporal images | change mask | whether a pixel/object changed |
| Semantic change detection | bi-temporal images | before/after or transition classes | what changed from which class to which class |
| Change captioning | bi-temporal images | natural-language description | describe salient changes |
| Text-guided change detection | images plus prompt/class text | mask, class, or score | language constrains the requested change |
| Change question answering | images plus question | answer | reason about a queried temporal relation |
| Remote-sensing VLM pretraining | image-text pairs | shared representation or generated text | learn transferable cross-modal knowledge |

## Method dimensions

1. **Spatial/temporal input:** co-registration, resolution, sensor, bands, patching, geographic shift, seasonal and illumination variation.
2. **Visual encoder:** CNN, ViT, hierarchical transformer, frozen foundation encoder, or task-specific encoder; shared versus separate temporal weights.
3. **Text pathway:** class names, captions, prompts, questions, generated pseudo-text, tokenizer, text encoder, and whether text is available at training, inference, or both.
4. **Alignment:** global contrastive, token/patch, region/text, class-prototype, grounding, or generative alignment.
5. **Temporal interaction:** early concatenation/difference, cross-attention, symmetric exchange, explicit correspondence, memory/state-space modeling, or late decision fusion.
6. **Cross-modal fusion:** injection location, direction, granularity, gating, query tokens, adapters, prompt tuning, and frozen/trainable boundaries.
7. **Prediction head:** segmentation decoder, transition classifier, autoregressive language decoder, retrieval head, or unified instruction-following decoder.
8. **Objectives:** segmentation/classification, contrastive, matching, caption likelihood, distillation, consistency, pseudo-label, grounding, or multi-task losses.
9. **Training design:** pretraining source, fine-tuning stages, weak or synthetic supervision, class balance, negative sampling, and augmentation.

## Evidence dimensions

- Dataset origin, sensor/resolution, image count, class distribution, split independence, geographic leakage, public availability, and license.
- Metrics appropriate to the task: precision/recall/F1/IoU/Kappa/OA for masks or classes; BLEU/METEOR/ROUGE/CIDEr/SPICE for captions; retrieval/QA metrics where relevant.
- Baseline comparability: same data split, backbone, resolution, pretraining, parameter budget, and inference inputs.
- Ablations that isolate the text pathway, temporal interaction, fusion site, objectives, and pretraining.
- Efficiency: trainable/total parameters, FLOPs, image size, batch size, precision, devices, training time, peak memory, and inference latency.
- Reproducibility: official code, commit/release, checkpoint, configuration, dataset preparation, seeds, and license.

## Common failure modes

- Treating seasonal, illumination, cloud, or registration differences as semantic change.
- Language priors overriding visible evidence or hallucinating change.
- Captions omitting small but operationally important changes.
- Closed-vocabulary prompts hiding poor open-world transfer.
- Geographic or scene leakage inflating test scores.
- Comparing captioning or segmentation metrics across different splits or preprocessing.
- Improvement arising from a larger pretrained backbone rather than the proposed fusion module.
- A module working only with private captions, synthetic instructions, or costly pretraining unavailable to the user.

## Practical filter for this project

Prioritize methods that can be evaluated on public datasets, fit or can be diagnostically tested on one A800 80GB, expose code or enough implementation detail, and teach transferable VLM/alignment/training skills. Record exceptions rather than hiding them.
