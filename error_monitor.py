from app_system import run_system

def monitor():
    try:
        result = run_system()
        return {"status": "success", "message": result}
    except Exception as e:
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "message": str(e)
        }
