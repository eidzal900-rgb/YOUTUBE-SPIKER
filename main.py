from engines.spike_detector import detect_spikes
from engines.niche_ranker import rank_niches
from engines.ai_script_engine import generate_scripts

def main():

    print("Scanning viral videos...")

    detect_spikes()

    print("Ranking niches...")

    rank_niches()

    print("Generating AI scripts...")

    generate_scripts()

    print("System completed")

if __name__ == "__main__":
    main()
