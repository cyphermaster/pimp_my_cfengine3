#!/usr/bin/php
<?php
require_once('/usr/share/pear/XML/RPC.php');


$client = new XML_RPC_Client('/', 'localhost', '8080');

$response = $client->send(
    new XML_RPC_Message('format',array(
	        XML_RPC_Encode("Toto"),
    	    XML_RPC_Encode(33) 
		)
	)
);

print $response->value()->getval()."\n";


# vim: ts=4:sw=4:ai
