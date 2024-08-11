-- some comment

DELIMITER //

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.quantity
	WHERE name = NEW.item_name;
END //

DELIMITER ;
