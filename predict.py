import argparse
from pathlib import Path
from app.matcher import calculate_match

def read_file(path):
    p = Path(path)
    if not p.exists(): raise FileNotFoundError(f"File not found: {path}")
    return p.read_text(encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="AI Resume & Job Matcher")
    parser.add_argument("--resume", required=True); parser.add_argument("--job", required=True)
    args = parser.parse_args(); r = calculate_match(read_file(args.resume), read_file(args.job))
    print("\nAI RESUME MATCH REPORT\n======================")
    print(f"Overall Match:   {r.match_score:.1f}%\nText Similarity: {r.text_similarity:.1f}%\nSkill Match:     {r.skill_match:.1f}%")
    print("\nMatched Skills:"); [print(f"  ✓ {s}") for s in r.matched_skills] or print("  None detected")
    print("\nMissing Skills:"); [print(f"  - {s}") for s in r.missing_skills] or print("  None detected")

if __name__ == "__main__": main()
