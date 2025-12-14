import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class IValidationRule(ABC):
    """Interface untuk aturan validasi registrasi mahasiswa."""

    @abstractmethod
    def validate(self, student):
        """Memvalidasi data mahasiswa."""
        pass


class SksLimitRule(IValidationRule):
    """Validasi batas maksimum SKS."""

    def validate(self, student):
        if student["sks"] > 24:
            logging.warning("SKS melebihi batas maksimum")
            return False
        logging.info("Validasi SKS berhasil")
        return True


class RegistrationService:
    """Service untuk registrasi mahasiswa."""

    def __init__(self, rules):
        self.rules = rules

    def register(self, student):
        """Menjalankan proses registrasi mahasiswa."""
        logging.info("Memulai proses registrasi")
        for rule in self.rules:
            if not rule.validate(student):
                logging.error("Registrasi gagal")
                return False
        logging.info("Registrasi berhasil")
        return True


if __name__ == "__main__":
    student = {"name": "Budi", "sks": 26}
    service = RegistrationService([SksLimitRule()])
    service.register(student)
