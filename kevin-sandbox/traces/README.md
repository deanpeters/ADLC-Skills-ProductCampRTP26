# Synthetic traces

The server appends every dispatched tool call to `trace.jsonl`. Each row identifies itself as synthetic and records the era, time, arguments, effective permission, baseline approval, result, and any block reason.

Generated traces are ignored by Git. They may include model-generated text. Do not put real customer information into this exercise.

Blocked attempts are evidence that the server guard worked, not evidence that the action occurred. A successful October action can still violate the May baseline. Counts describe this exercise only; they do not establish real customer outcomes.
