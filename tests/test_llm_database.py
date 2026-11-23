from scanner.llm_database import LLM_DATABASE


def test_names_and_ollama_tags_are_unique():
    names = [m.name for m in LLM_DATABASE]
    tags = [m.ollama_tag for m in LLM_DATABASE]
    assert len(set(names)) == len(names)
    assert len(set(tags)) == len(tags)


def test_minimum_requirements_do_not_exceed_recommended():
    for m in LLM_DATABASE:
        assert 0 < m.min_vram_gb <= m.rec_vram_gb, m.name
        assert 0 < m.min_ram_gb <= m.rec_ram_gb, m.name


def test_cpu_inference_needs_at_least_as_much_memory_as_gpu():
    for m in LLM_DATABASE:
        assert m.min_ram_gb >= m.min_vram_gb, m.name
