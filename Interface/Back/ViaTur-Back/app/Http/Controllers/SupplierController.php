<?php

namespace App\Http\Controllers\SupplierController;

use App\Models\Supplier;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller;


class SupplierController extends Controller
{
    public function update(Request $request)
    {
        $form = new Supplier($request->only(['data','price','description','address','selectedOption']));
        $insert = $form->save();

        if ($insert) {
            return response(status: 200);
        } else {
            return response(status: 500);
        }
    }
    public function store(Request $request)
    {
        $form = new Supplier($request->only(['data','price','description','address','selectedOption']));
        $insert = $form->save();

        if ($insert) {
            return response('deu certo','200');
        } else {
            return response(status: 500);
        }
    }
}
