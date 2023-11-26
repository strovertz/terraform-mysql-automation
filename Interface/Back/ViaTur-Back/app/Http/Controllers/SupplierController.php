<?php

namespace App\Http\Controllers;

use App\Models\Supplier;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;

class SupplierController
{
    public function post(Request $request) : jsonResponse
    {
        error_log("aqui");
        $form = new Supplier($request->only(['data','price','description','address','selectedOption']));
        $insert = $form->save();

        if ($insert) {
            return response()->json('deu certo','200');
        } else {
            return response()->json(status: 500);
        }
    }

    public function index(Request $request) : jsonResponse
    {

            return response()->json('deu certo','200');

    }
}
