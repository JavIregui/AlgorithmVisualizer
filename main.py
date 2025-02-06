import sys
from app import AlgorithmVisualizer

def main():
    try:
        app = AlgorithmVisualizer()
        app.run()
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()