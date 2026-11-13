async def task(input):
    """주제 하나로 lead를 실행하고, 보고서와 lead의 도구 호출 수를 돌려준다."""
    cfg = {"configurable": {"thread_id": f"eval-{uuid.uuid4().hex[:6]}"}}
    # 재작성 질문에서 일시 중지
    await lead.ainvoke({"messages": [{"role": "user", "content": input["topic"]}]}, cfg)
    # 평가에서는 다시 쓰지 않고 끝낸다
    state = await lead.ainvoke(Command(resume="n"), cfg)
    calls = [c for m in state["messages"] if m.type == "ai" for c in m.tool_calls]
    return {"report": Path(state["report"]).read_text(), "steps": len(calls)}


def success(output, expected):
    """필수 키워드가 보고서에 모두 들어 있으면 성공"""
    return all(k in output["report"] for k in expected["keywords"])

def steps(output):
    """lead가 호출한 도구 수"""
    return output["steps"]

await client.experiments.run_experiment(
    dataset=dataset, task=task, evaluators=[success, steps],
    experiment_name="multi-agent", timeout=600)  # Multi Agent 한 번 실행에 1-2분이 걸린다
