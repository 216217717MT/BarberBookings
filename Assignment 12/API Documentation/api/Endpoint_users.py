
@app.get("/api/oppointment", response_model=List[User], tags=["appointments"])
def list_oppointments():
    return oppointment_service.list_oppointments()