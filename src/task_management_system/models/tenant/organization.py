"""File containing the Organization Class model."""


class Organization:
    """Class representing an organization in the task management system."""

    def __init__(self, name: str, address: str, contact_email: str):
        """Initialize an Organization instance.

        Args:
            name (str): The name of the organization.
            address (str): The physical address of the organization.
            contact_email (str): The contact email for the organization.
        """
        self.name = name
        self.address = address
        self.contact_email = contact_email

    def __repr__(self) -> str:
        """Return a string representation of the Organization instance."""
        return f"Organization(name={self.name}, address={self.address}, contact_email={self.contact_email})"

    def __str__(self) -> str:
        """Return a user-friendly string representation of the Organization instance."""
        return f"{self.name} located at {self.address}. Contact: {self.contact_email}"


if __name__ == "__main__":
    # Example usage
    org = Organization(
        "Tech Solutions",
        "123 Tech Lane, Silicon Valley, CA",
        "contact@techsolutions.com",
    )
    print(org)
