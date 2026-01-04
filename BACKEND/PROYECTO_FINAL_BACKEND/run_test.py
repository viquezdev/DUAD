import pytest
import sys

def run_all_tests():
    print("Starting Automated Test Suite...\n")
    
    args = ["-v", "--tb=short", "-s"]
    
    exit_code = pytest.main(args)
    
    if exit_code == 0:
        print("\nSUCCESS: All tests passed!")
    else:
        print("\nFAILURE: Some tests did not pass. Check the report above.")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    run_all_tests()